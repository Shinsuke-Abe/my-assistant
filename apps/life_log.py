import json
import logging
import os
import time
import uuid
try:
    import unzip_requirements
except ImportError:
    pass
import jsonschema
import boto3

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


def auth(event, context):
    token = event['authorizationToken'] \
            if event['authorizationToken'] is not None \
            else event['header']['headers']['authorization']
    client = boto3.client('cognito-idp')

    try:
        data = client.get_user(
            AccessToken=token
        )
        logging.info(data)

        return generate_policy('user', 'Allow', event['methodArn'])
    except Exception as e:
        logging.error("AuthError:{0}".format(e))
        return generate_policy('user', 'Deny', event['methodArn'])


def generate_policy(principal_id, effect, resource):
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': effect,
                'Resource': resource
            }]
        }
    }
