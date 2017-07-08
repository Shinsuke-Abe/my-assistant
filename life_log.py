# coding:utf-8
import json
import logging
import os
import time
import uuid

import boto3


def get_dynamodb(event):
    if 'isOffline' in event and event['isOffline'] is True:
        return boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name='ap-northeast-1')
    else:
        return boto3.resource('dynamodb')


def create_life_log(event, context):
    """event.bodyに指定されたライフログをDynamoDBに登録します。
    >>> create_life_log({"isOffline": True}, {})
    Traceback (most recent call last):
    Exception: Coudn't create life log.Detail:'body'
    >>> create_life_log({"isOffline": True, "body":"{}"}, {})
    Traceback (most recent call last):
    Exception: Coudn't create life log.Detail:'event'
    """
    print(event)
    try:
        dynamodb = get_dynamodb(event)
        timestamp = int(time.time() * 1000)

        data = json.loads(event['body'])
        table = dynamodb.Table(os.environ['LIFE_EVENT_TABLENAME'])

        item = {
            'id': str(uuid.uuid1()),
            'event': data['event'],
            'createdAt': timestamp,
            'updatedAt': timestamp
        }

        if 'insight' in data:
            item['insight'] = data['insight']

        table.put_item(Item=item)

        response = {
            "statusCode": 200,
            "body": json.dumps(item)
        }

        return response
    except KeyError as e:
        logging.error("Validation Failed")
        raise Exception("Coudn't create life log.Detail:{0}".format(e))
        return

if __name__ == "__main__":
    import doctest
    doctest.testmod()
