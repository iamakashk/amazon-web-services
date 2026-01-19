import os
import json

def lambda_handler(event, context):
    app_name = os.environ.get("APP_NAME", "UnknownApp")
    environment = os.environ.get("ENV", "dev")
    timeout = os.environ.get("APP_TIMEOUT", "not-set")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "app_name": app_name,
            "environment": environment,
            "timeout": timeout
        })
    }
