import json
import boto3
import os


def generate_swagger(event, context):
    client = boto3.client('apigateway')

    staged_apis = [api for api in client.get_rest_apis()['items']
                   if api['name'] == os.environ['REST_API_NAME']]

    print(staged_apis.pop())

    return
