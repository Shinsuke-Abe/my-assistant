# 概要

自分のアシスタントをしてくれるサービスを目指します。

という体のServerlessアーキテクチャ実験場です。

# テストするときには

isOfflineをeventに追加しよう。そうするとローカルのDynamoDBにアクセスする。

# インストールが必要なもの一覧

* jsonschema:jsonschemaをpythonで使うパッケージ
* serverless-dynamodb-local:dynamodb localをserverlessフレームワークから利用するためのプラグイン
* serverless-aws-documentation:serverless.ymlにドキュメント情報を追記するためのプラグイン
* bats:bashコマンドをテストするためのフレームワーク
