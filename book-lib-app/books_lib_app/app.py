import json
import boto3 
import os 

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('BOOKS_TABLE')

def lambda_handler(event, context):
    
    print(event)
    # order = json.loads(event["body"])

    # table = dynamodb.Table(table_name)
    # response = table.put_item(Item=order)
    
    # print(response)
    
    return {
        "statusCode" : 201,
        "headers" : {},
        "body" : json.dumps({"message": "Fake Massage"})
    }