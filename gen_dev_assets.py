import json
import boto3
import os


def generate_swagger(event, context):
    client = boto3.client('apigateway')

    staged_api = [api for api in client.get_rest_apis()['items']
                  if api['name'] == os.environ['REST_API_NAME']].pop()

    exported_api = client.get_export(
        restApiId=staged_api['id'],
        stageName=os.environ['REST_API_STAGE_NAME'],
        exportType="swagger"
    )

    print(exported_api)

    return
