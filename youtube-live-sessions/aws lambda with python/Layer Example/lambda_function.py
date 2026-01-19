import json
from utils import format_response

def lambda_handler(event, context):
    response = format_response("Hello from Lambda Layer")
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
