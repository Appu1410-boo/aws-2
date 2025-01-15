import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket_name = 'your-s3-bucket-name'
        # Extract the file name and content from the event
        file_name = event['file_name']  # e.g., "example.pdf"
        file_content = event['file_content']  # Base64-encoded content of the file
        file_data = base64.b64decode(file_content)
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_data)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f"File '{file_name}' successfully uploaded to bucket '{bucket_name}'."
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
