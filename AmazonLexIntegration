import json

def lambda_handler(event, context):
    # Extract the user input from the Lex event
    user_message = event['inputTranscript']
    
    # Create a response message
    response_message = f"You said: {user_message}"
    
    # Build the response event for Amazon Lex
    response = {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": response_message,
            },
        },
    }

    return response
