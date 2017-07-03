import json


def create_life_log(event, context):
    try:
        id_value = event["id"]

        print(id_value)

        response = {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Go Serverless v1.0! "
                           "Your function named create_life_log "
                           "executed successfully(separated python file)!",
                "input": event
            })
        }
    except KeyError:
        response = {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Your function named create_life_log executed,"
                           "but not found required input!"
            })
        }

    return response
