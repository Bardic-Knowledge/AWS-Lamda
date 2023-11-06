import json

def lambda_handler(event, context):
    # Extract the HTTP method and request body from the event
    http_method = event['httpMethod']
    request_body = event.get('body', None)

    if http_method == 'GET':
        response_body = {"message": "This is a GET request."}
    elif http_method == 'POST':
        if request_body:
            request_data = json.loads(request_body)
            response_body = {"message": "This is a POST request with data:", "data": request_data}
        else:
            response_body = {"message": "This is a POST request with no data."}
    else:
        response_body = {"message": "Unsupported HTTP method."}

    # Create the HTTP response
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(response_body)
    }

    return response
