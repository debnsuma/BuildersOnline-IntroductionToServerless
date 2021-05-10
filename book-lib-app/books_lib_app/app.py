import simplejson as json
import boto3 
import os 
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('BOOKS_TABLE')

def lambda_handler(event, context):
    
    table = dynamodb.Table(table_name)
    method_type = event["httpMethod"]
    
    # Get list of books from library (All Books and Single Book)
    if method_type == "GET":
        
        # When Book ID is provided
        if event["queryStringParameters"]:
            book_isbn = int(event["queryStringParameters"]["isbn_id"])
            book = table.query(KeyConditionExpression=Key("isbn_id").eq(book_isbn))
        
        # When Book ID is NOT provided       
        else:
            book = table.scan()
        
        return {
            'statusCode' : 200,
            'headers' : {},
            'body' : json.dumps(book['Items'])
            }
    
    # Add book(s) to the library
    if method_type == "POST":
        
        book_data = json.loads(event["body"])
        
        for each_book in book_data:
            table.put_item(Item=each_book)
        
        return {
            "statusCode" : 201,
            "headers" : {},
            "body" : json.dumps({"message": "Books data updated"})
        }
    
    # Delete a book from the library
    if method_type == "DELETE":
        
        # When Book ID is provided
        if event["queryStringParameters"]:
            book_isbn = int(event["queryStringParameters"]["isbn_id"])
            table.delete_item(Key={"isbn_id": book_isbn})
        
        return {
            "statusCode" : 201,
            "headers" : {},
            "body" : json.dumps({"message": f"Book deleted with isbn : {book_isbn}"})
        }