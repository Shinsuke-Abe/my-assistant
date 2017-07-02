import json


def create_life_log(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function named create_life_log "
                   "executed successfully(separated python file)!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
