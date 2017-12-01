import boto3
import json
import os

client = boto3.client('cognito-idp')


def sign_up(event, context):
    response = client.sign_up(
        ClientId=os.environ['COGNITO_POOL_CLIENT_ID'],
        Username=event['Username'],
        Password=event['Password'],
        UserAttributes=[
            {
                'Name': 'email',
                'Value': event['email']
            },
            {
                'Name': 'custom:custom-attributes',
                'Value': event['custom']
            }
        ]
    )

    return response


def confirm(event, context):
    response = client.confirm_sign_up(
        ClientId=os.environ['COGNITO_POOL_CLIENT_ID'],
        Username=event['Username'],
        ConfirmationCode=event['ConfirmationCode']
    )

    return response


def sign_in(event, context):
    response = client.admin_initiate_auth(
        UserPoolId=os.environ['COGNITO_POOL_ID'],
        ClientId=os.environ['COGNITO_POOL_CLIENT_ID'],
        AuthFlow="ADMIN_NO_SRP_AUTH",
        AuthParameters={
            "USERNAME": event['Username'],
            "PASSWORD": event['Password'],
        }
    )

    return response


def refresh_token(event, context):
    response = client.initiate_auth(
        ClientId=os.environ['COGNITO_POOL_CLIENT_ID'],
        AuthFlow="REFRESH_TOKEN",
        AuthParameters={
            "USERNAME": event['Username'],
            "REFRESH_TOKEN": event['refresh_token']
        }
    )

    return response
