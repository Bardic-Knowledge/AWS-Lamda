import json
import re

def lambda_handler(event, context):
    # Extract the API data from the event
    api_data = event.get('data', '')

    # Define the keyword to search for evidence of exfiltrated data or evidence of compromise
    keyword = ""

    # Check for the presence of the keyword
    if re.search(keyword, api_data, re.I):  # Using a case-insensitive search
        alert_message = f"Suspicious keyword '{keyword}' found in API data: {api_data}"
        # Send an alert (e.g., to CloudWatch Logs, an SNS topic, or a security system)

        # For demonstration purposes, we'll print the alert to CloudWatch Logs
        print(alert_message)
    else:
        # No keyword found, data is clean
        print("API data is clean")

    # You can return a response if needed
    response = {
        "statusCode": 200,
        "body": json.dumps("Inspection completed"),
    }

    return response
