import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create_life_log(event, context):
    try:
        timestamp = int(time.time() * 1000)

        table = dynamodb.Table(os.environ['LIFE_EVENT_TABLENAME'])

        item = {
            'id': str(uuid.uuid1()),
            'event': event['event'],
            'createdAt': timestamp,
            'updatedAt': timestamp
        }

        if 'insight' in event:
            item['insight'] = event['insight']

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
