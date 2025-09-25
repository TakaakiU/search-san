# lambda/main.py
import os
import psycopg2
import random
from datetime import datetime

def lambda_handler(event, context):
    """
    AWS Lambdaが実行するメインの関数。
    """
    print("処理開始...")

    try:
        # AWS Lambda環境では、環境変数から接続情報を取得
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            port=os.environ.get("DB_PORT")
        )
        print("データベース接続成功")
    except Exception as e:
        print(f"データベース接続エラー: {e}")
        return {"statusCode": 500, "body": "DB Connection Error"}

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, url, title FROM search_article WHERE status = 'ACTIVE';")
            articles = cur.fetchall()
            print(f"{len(articles)}件の記事を取得しました。")
    except Exception as e:
        print(f"記事取得エラー: {e}")
        conn.close()
        return {"statusCode": 500, "body": "Article Fetch Error"}

    results_count = 0
    for article in articles:
        article_id, article_url, article_title = article
        print(f"処理中: {article_title or article_url}")
        
        try:
            # ダミーの順位を1〜100位でランダムに生成
            rank = random.randint(1, 100)
            print(f"  -> 順位: {rank}位")

            with conn.cursor() as cur:
                insert_query = """
                    INSERT INTO search_serpresult (id, article_id, search_engine, rank, checked_at)
                    VALUES (gen_random_uuid(), %s, %s, %s, %s);
                """
                cur.execute(insert_query, (article_id, 'GOOGLE', rank, datetime.now()))
            
            results_count += 1
        except Exception as e:
            print(f"  -> エラー: {e}")
            conn.rollback()
            continue

    conn.commit()
    conn.close()
    print(f"{results_count}件の結果を保存しました。")
    print("処理完了")
    
    return {
        "statusCode": 200,
        "body": f"Processed {len(articles)} articles, saved {results_count} results."
    }

# --- このファイルが直接実行された場合のみ、以下のコードが動く ---
if __name__ == "__main__":
    # この部分はローカルでのテスト実行専用
    print("ローカルテストモードで実行します...")

    # Dockerで起動しているローカルDBに接続するための設定
    # これらの値はdocker-compose.ymlで定義したものと一致させる
    local_db_config = {
        "DB_HOST": "localhost",
        "DB_NAME": "search_san_db",
        "DB_USER": "django",
        "DB_PASSWORD": "secret",
        "DB_PORT": "5432"
    }
    
    # 環境変数を設定
    for key, value in local_db_config.items():
        os.environ[key] = value
    
    # ハンドラーを実行
    lambda_handler(None, None)
    