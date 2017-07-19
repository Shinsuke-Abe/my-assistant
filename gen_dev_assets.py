import boto3
import os

apigateway = boto3.client('apigateway')
s3 = boto3.resource('s3')


def generate_swagger(event, context):
    staged_api = [api for api in apigateway.get_rest_apis()['items']
                  if api['name'] == os.environ['REST_API_NAME']].pop()

    exported_api = apigateway.get_export(
        restApiId=staged_api['id'],
        stageName=os.environ['REST_API_STAGE_NAME'],
        exportType="swagger"
    )

    swagger_bucket = s3.Bucket(os.environ['SWAGGER_FILE_BUCKET'])

    swagger_file = swagger_bucket.Object('swagger.json')
    swagger_file.put(
        Body=exported_api['body'].read().decode('utf-8'),
        ContentEncoding='utf-8',
        ContentType='text/plane',
        ACL='public-read'
    )

    return
