# TODO 請求
# 1. 月度とプロジェクトを指定してキック
# 2. PDFでレポートを指定する
# 3. PDFをGoogleドライブに保存する
# 4. misocaのAPIから請求書の金額を登録
# 5. メールで送る
# 各APIのシークレットキーは暗号化してDynamoDBに保存する
# 各ステップはLambdaファンクションとして作ってStepFunctionsでつなぐ
# API Gatewayで公開するのはStepFunctionsのみ(要認証)
# Step Functionsは切り出す

# TODO プロジェクトの締め日を取得(要認証)

# TODO プロジェクトの締日を登録(要認証)

# TODO プロジェクトの担当者を取得する(要認証)

# TODO プロジェクトの担当者を登録する(要認証)

# TODO 登録ずみサービスキーリストを取得する(要認証)

# TODO サービス、URL、キーを取得する(要認証)

# TODO サービス、URL、キーを登録する(要認証)
# 検索キーとなる項目はサービス名
# APIキーとURL
# APIキーはKMSで暗号化する
# KMSのキーエイリアスはalias/MyAssistantCMKAlias
# resources.ymlに追加
# テーブル名。。。externalAPIs
