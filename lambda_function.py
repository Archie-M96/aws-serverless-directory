import json
import boto3

# Initialize the DynamoDB connection
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LocumDirectory-Listings')

def lambda_handler(event, context):
    try:
        # Fetch all listings from our database
        response = table.scan()
        listings = response.get('Items', [])
        
        # Send the data back to the website successfully
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*', # This lets your S3 website securely talk to it
                'Content-Type': 'application/json'
            },
            'body': json.dumps(listings)
        }
    except Exception as e:
        # If something goes wrong, tell us what happened
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
