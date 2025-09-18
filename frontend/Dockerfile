FROM node:18-alpine

# 作業ディレクトリを設定
WORKDIR /frontend

# 2. package*.json を使用するのは良い方法です
COPY package*.json ./

# 依存関係をインストール
RUN npm install

# アプリケーションのコードをコピー
COPY . .
