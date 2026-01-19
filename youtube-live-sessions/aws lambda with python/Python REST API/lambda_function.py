import json

def lambda_handler(event, context):
    try:
        # Support API Gateway HTTP API (v2)
        method = event.get("httpMethod") or event.get("requestContext", {}) \
            .get("http", {}) \
            .get("method")

        if method == "GET":
            print("----------- METHOD IS : GET -----------")
            return response(200, {
            "message": "Order placed successfully and email sent-GET REQUEST"
            })

        if method == "POST":
            print("----------- METHOD IS : POST -----------")
            raw_body = event.get("body")
            order = json.loads(raw_body)
            order_id = order.get("orderId")
            email = order.get("email")
            return response(200, {
            "message": "Order placed successfully and email sent",
            "orderId": order_id,
            "email": email
        })
        
    except Exception as e:
        return response(500, {"error": str(e)})


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
