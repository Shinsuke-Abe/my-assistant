import json
import boto3
from infra import AESCipher


def hello(event, context):
    body = {
        "message": ("Go Serverless v1.0! Your function named hello executed"
                    " successfully!"),
        "input": event
    }

    plain_message = "message from human"
    print(plain_message)
    client = boto3.client('kms')
    encrypted_key = client.generate_data_key(
        KeyId="alias/MyAssistantCMKAlias",
        KeySpec="AES_256"
    )
    print(encrypted_key)
    plaintext_key = client.decrypt(
        CiphertextBlob=encrypted_key["CiphertextBlob"]
    )
    print(plaintext_key)

    cipher = AESCipher.AESCipher(plaintext_key["Plaintext"])
    encrypted_message = cipher.encrypt(plain_message)
    print(encrypted_message)

    print(cipher.decrypt(encrypted_message))

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event
    # with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
