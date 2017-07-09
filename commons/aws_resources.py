import boto3


def get_dynamodb(event):
    if 'isOffline' in event and event['isOffline'] is True:
        return boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:
        return boto3.resource('dynamodb')
