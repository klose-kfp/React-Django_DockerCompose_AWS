# F-IT 〜first-it〜

# テキストから、シーケンス図など各種 UML を作成する Web アプリ

このプロジェクトは、複数の AI を活用した Web アプリケーションです。
動作の概要については「動作の流れ.txt」を、
動作時の画面収録動画は[こちら](https://youtu.be/07NAbAeBqbc?si=Qslk7mJXpJko63_6)をご覧ください。

○ 使用ツール(「⭐︎」が今回のコードで使用)
・フロントエンド
⭐︎React (typescript)
・バックエンド
⭐︎Django (Python)
Node.js (JavaScript)
・使用 AI
⭐︎ChatGPT
⭐︎Mermaid
・Docker
⭐︎Docker Compose
(フロントエンド(nginx)・バックエンド のコンテナ 2 つ)
・サーバー
⭐︎AWS
(インターネット → CloudFront → EC2 → nginx → Docker Compose
ACM の証明書で HTTPS 化)
Heroku
・ドメイン
⭐︎ お名前.com
・DB
⭐︎SQLite
MySQL
PostgreSQL
Heroku アドオン (Heroku Postgres)

インストールと実行
このプロジェクトをローカルで実行するためには、以下の手順を実行してください。

リポジトリをクローンします。
フロントエンドとバックエンドの依存関係をインストールします。
Docker Compose を使用してアプリケーションを起動します。
詳細な手順については、インストールガイドを参照してください。

This software is released under the MIT License, see LICENSE.txt.
