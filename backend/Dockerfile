# ベースイメージとして公式のPythonイメージを使用
FROM python:3.13-slim

# 環境変数を設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを作成・設定
WORKDIR /app

# requirements.txt を先にコンテナにコピー
COPY requirements.txt /app/

# pipをアップグレードし、requirements.txt に記載されたパッケージをインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# プロジェクトのコードをコンテナにコピー
COPY . /app/
