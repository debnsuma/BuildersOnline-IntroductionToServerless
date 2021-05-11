# First App 

AWS Service to be used:
    - AWS Lambda 
    - Amazon S3 
    - Amazon Comprehend 

In this demo, we will describes the use of Amazon Comprehend to summarize text documents and create Lambda functions to analyze the texts. 
- We will learn how to develop services by applying the serverless computing paradigm, and use Amazon Comprehend to examine texts to determine their primary language. 
- We will extract information such as:
    - entities (people or places), 
    - key phrases (noun phrases that are indicative of the content), 
    - emotional sentiments

## Steps to follow:

- Create an S3 bucket 
- Go to AWS Lambda console and click on "Create Function" 
    - Select "Author from scratch" 
    - Give some name to your lambda function(e.g. 'first-function') 
    - Select the runtime as Python3.8
    - Click on Create Function 
- Go to "Configuration" tab 
    - Go to execution Role 
    - Add a new role, give some name 
    - From the "Policy templates" drop down select : Amazon S3 object read-only permission 
    - Also add "ComprehendFullAccess" policy to the role

- Come back to the lambda function page 
    - Click on "Add Trigger"
    - Select "s3" under "Trigger Configuration"
    - Select "Bucket" : Name of the bucket you created earlier -> "Event Type" : "All object create event"
    - Click on "Add"

- Edit the lambda_function
- Save the funtion and click on Deploy 
- Test the function by uploading some file with some text in your S3 bucket, e.g. "test_file.txt"
- Check the logs 


    