import json
import logging
import os
import time
import uuid

import boto3


def get_dynamodb(event):
    if 'isOffline' in event and event['isOffline'] is True:
        return boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:
        return boto3.resource('dynamodb')


def create_life_log(event, context):
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
