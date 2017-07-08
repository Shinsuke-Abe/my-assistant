#!/usr/bin/env bats

@test "入力が渡されない場合はbodyの取得でエラーになる" {
  error_message="Exception: Coudn't create life log.Detail:'body'"
  sls invoke local -f create_life_log | grep "$error_message"
  [ $? -eq 0 ]
}

# """event.bodyに指定されたライフログをDynamoDBに登録します。
# >>> create_life_log({"isOffline": True, "body":"{}"}, {})
# Traceback (most recent call last):
# Exception: Coudn't create life log.Detail:'event'
# """
