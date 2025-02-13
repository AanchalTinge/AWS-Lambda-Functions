import boto3
import base64
import json
import os

# Initialize S3 client
s3 = boto3.client("s3")

# Define S3 bucket name (replace with your bucket name)
BUCKET_NAME = "your-s3-bucket-name"

def lambda_handler(event, context):
    try:
        # Get file data from the event (Base64 encoded)
        file_content = event.get("file_content", "")
        file_name = event.get("file_name", "default.pdf")

        if not file_content:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No file content provided."})
            }

        # Decode the Base64 file content
        decoded_file = base64.b64decode(file_content)

        # Upload the file to S3
        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=decoded_file)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "File uploaded successfully!", "file_name": file_name})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
