# Search San（サーチさん）

`Search San` は、指定したドメインの記事リストを管理し、主要な検索エンジンにおける検索順位（SERP）を自動で追跡・可視化するためのWebアプリケーションです。

モダンなWeb技術スタック（React, Django, PostgreSQL）とAWSサーバーレスアーキテクチャ（Lambda, EventBridge）を組み合わせることで、スケーラブルでメンテナンス性の高いシステムを目指しています。

## ✨ 主な機能（開発中）

- **ドメイン管理:** 追跡対象のドメインを登録・管理します。
- **記事管理:** ドメインに紐づく記事を登録・管理します。
- **SERP自動計測:** AWS LambdaとEventBridgeを利用して、検索順位を毎日自動で取得・記録します。
- **結果の可視化:** 計測した検索順位の推移をグラフなどで表示します。

## 🚀 技術スタック

このプロジェクトで使用されている主要な技術は以下の通りです。

| カテゴリ           | 技術                                |
| ------------------ | ----------------------------------- |
| **フロントエンド** | React, React Router, Axios          |
| **バックエンド**   | Django, Django REST Framework       |
| **データベース**   | PostgreSQL                          |
| **バッチ処理**     | AWS Lambda (Python)                 |
| **スケジューラ**   | AWS EventBridge                     |
| **インフラ**       | AWS (RDS, VPC, ECR), Docker         |
| **CI/CD**          | GitHub Actions (予定)               |

## 💻 開発環境のセットアップ

このプロジェクトをローカルで実行するには、以下のツールが必要です。

- Docker
- Docker Compose

### セットアップ手順

1. **リポジトリをクローン:**

    ```bash
    git clone https://github.com/your-username/search-san.git
    cd search-san
    ```

2. **バックエンド用の`.env`ファイルを作成:**
    `backend/`ディレクトリに`.env`ファイルを作成し、以下の内容を記述します。

    ```env
    # backend/.env
    DB_NAME=search_san_db
    DB_USER=django
    DB_PASSWORD=secret
    DB_HOST=db
    DB_PORT=5432
    SECRET_KEY='your-django-secret-key' # 任意の秘密キーを設定
    DEBUG=True
    ```

    > `SECRET_KEY`は、ローカルの`backend/config/settings.py`からコピーするか、[Djecrety](https://djecrety.ir/)のようなツールで新しく生成してください。

3. **Dockerコンテナをビルドして起動:**
    プロジェクトのルートディレクトリで以下のコマンドを実行します。初回起動には数分かかります。

    ```bash
    docker-compose up --build
    ```

4. **データベースのマイグレーション:**
    コンテナが起動したら、**別のターミナル**を開き、以下のコマンドを実行してデータベースのテーブルを作成します。

    ```bash
    docker-compose run --rm web python manage.py migrate
    ```

5. **管理者ユーザーの作成（任意）:**
    Djangoの管理サイトにアクセスするために、管理者ユーザーを作成します。

    ```bash
    docker-compose run --rm web python manage.py createsuperuser
    ```

### アプリケーションへのアクセス

セットアップが完了すると、以下のURLで各サービスにアクセスできます。

- **React SPA:** `http://localhost:3000`
- **Django REST API:** `http://localhost:8000/api/`
- **Django管理サイト:** `http://localhost:8000/admin/`

## 🧪 APIのテスト

プロジェクトのルートディレクトリにある`api-tests.http`ファイルを使用すると、[REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) (VS Code拡張機能) を使ってAPIエンドポイントを簡単にテストできます。

1. `api-tests.http`ファイルを開きます。
2. テストしたいリクエストブロックの上にある「Send Request」をクリックします。

## ☁️ AWSリソース

このプロジェクトは、以下のAWSサービスを利用してクラウド上で動作します。

- **AWS RDS for PostgreSQL:** 本番データベース
- **AWS Lambda:** 検索順位を計測するバッチ処理
- **AWS EventBridge:** Lambda関数を定期実行するスケジューラ
- **AWS VPC / Security Group:** セキュアなネットワーク環境
- **AWS ECR:** Django APIのDockerイメージ保管場所
- **AWS App Runner:** Django APIのホスティング（予定）
- **Amazon S3 / CloudFront:** React SPAのホスティング（予定）

## 📜 ライセンス

このプロジェクトは [MIT License](LICENSE) の下で公開されています。
