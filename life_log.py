import json
import logging
import os
import time
import uuid
import unzip_requirements
import jsonschema

from commons import aws_resources


def create_life_log(event, context):
    try:
        dynamodb = aws_resources.get_dynamodb(event)
        timestamp = int(time.time() * 1000)

        data = json.loads(event['body'])
        request_schema = json.load(open(os.environ['REQUEST_MODEL_SCHEMA']))
        jsonschema.validate(data, request_schema)
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
