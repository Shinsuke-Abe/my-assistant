#!/usr/bin/env bats

@test "入力が渡されない場合はbodyの取得でエラーになる" {
  error_message="Exception: Coudn't create life log.Detail:'body'"
  run sls invoke local -f create_life_log -d '{"isOffline":true}'
  [ "$status" -eq 0 ]

  run assert_contains_message $error_message ${lines[@]}
  [ "$status" -eq 0 ]
}

@test "入力にevent属性がない場合はエラーになる" {
  error_message="Exception: Coudn't create life log.Detail:'event'"
  run sls invoke local -f create_life_log -d '{"isOffline":true, "body":"{}"}'
  [ "$status" -eq 0 ]

  echo ${lines[@]}

  run assert_contains_message $error_message ${lines[@]}
  [ "$status" -eq 0 ]
}

@test "入力にevent属性がある時は登録される" {
  run sls invoke local -f create_life_log -d '{"isOffline":true, "body":"{\"event\":\"test event\"}"}'
  [ "$status" -eq 0 ]
  # TODO ステータスコードの確認の仕方
  # status_code='"statusCode": 200,'
  # echo ${lines[@]}
  # run assert_contains_message $status_code ${lines[@]}
  # [ "$status" -eq 0 ]
}

assert_contains_message() {
  local expected=$1
  shift
  local actual_message=($@)

  for line in ${actual_message[@]}
  do
    echo $line
    if [ $expected = $line ];then
      # contains
      return 0
    fi
  done
  # not found
  return 1
}

# """event.bodyに指定されたライフログをDynamoDBに登録します。
# >>> create_life_log({"isOffline": True, "body":"{}"}, {})
# Traceback (most recent call last):
# Exception: Coudn't create life log.Detail:'event'
# """
