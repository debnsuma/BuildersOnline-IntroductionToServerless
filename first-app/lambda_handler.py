import boto3
import json 
import os 

# create a comprehend object
comprehend = boto3.client(service_name="comprehend")

# create a s3 object 
s3 = boto3.client("s3")

def lambda_handler(event, context):
    
    # check if an event is True 
    if event:
        
        
        # event – AWS Lambda uses this parameter to pass in event data to the handler. 
        # This parameter is usually of the Python dict type. It can also be list, str, int, float, or NoneType type
        text_file_obj = event["Records"][0]
        # assign the uploaded text file name to the 'filename' variable 
        
        filename = str(text_file_obj['s3']['object']['key'])
        bucket_name = text_file_obj['s3']['bucket']['name']
        
        file_obj = s3.get_object(Bucket = bucket_name, Key = filename)
        
        # access the file_obj's body. Invoke the read() function and convert to a str object. 
        # assign to the variable 'body_str_obj' 
        body_str_obj = str(file_obj['Body'].read())
        
        # call detect_sentiment()
        sentiment_response = comprehend.detect_sentiment(Text = body_str_obj, LanguageCode = "en")
        print("Sentiment_response: \n", sentiment_response)
        
        # call detect_entities()
        entity_response = comprehend.detect_entities(Text = body_str_obj, LanguageCode = "en")
        print("\n\nEntity_response: \n", entity_response)
        
        # call detect_key_phrases()
        key_phases_response = comprehend.detect_key_phrases(Text = body_str_obj, LanguageCode = "en") 
        print("\n\nKey_phases_response: \n", key_phases_response)
      
        return {
            'statusCode' :200,
            'body' : json.dumps('Hello from Lambda')
        }
    
