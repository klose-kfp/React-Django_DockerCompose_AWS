# F-IT 〜first-it〜

# テキストからシーケンス図など各種 UML を作成する Web アプリ

このプロジェクトは、複数の AI を活用した Web アプリケーションです。<br>
動作の概要については「動作の流れ.txt」を、<br>
動作時の画面収録動画は<br>
[こちら](https://youtu.be/07NAbAeBqbc?si=Qslk7mJXpJko63_6)をご覧ください。<br>
<br>
○ 使用ツール(「⭐︎」が今回のコードで使用)<br>
・フロントエンド<br>
⭐︎React (typescript)<br>
・バックエンド<br>
⭐︎Django (Python)<br>
Node.js (JavaScript)<br>
・使用 AI<br>
⭐︎ChatGPT<br>　
⭐︎Mermaid<br>　
・Docker<br>
⭐︎Docker Compose<br>　
(フロントエンド(nginx)・バックエンド のコンテナ 2 つ)<br>
・サーバー<br>
⭐︎AWS<br>
(インターネット → CloudFront → EC2 → nginx → Docker Compose<br>
ACM の証明書で HTTPS 化)<br>
Heroku<br>
・ドメイン<br>
⭐︎ お名前.com<br>
・DB<br>
⭐︎SQLite<br>
MySQL<br>
PostgreSQL<br>
Heroku アドオン (Heroku Postgres)<br>
<br>
This software is released under the MIT License, see LICENSE.txt.
