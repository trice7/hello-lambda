import json
import boto3


def lambda_handler(event, context):
    print("Received S3 event:", json.dumps(event))

    s3 = boto3.client('s3')

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        event_name = record['eventName']

        print(f"Event Name: {event_name}")
        print(f"Bucket Name: {bucket_name}")
        print(f"Object Key: {object_key}")

        # Get the uploaded file
        response = s3.get_object(
            Bucket=bucket_name,
            Key=object_key
        )

        # Read the existing text
        existing_text = response['Body'].read().decode('utf-8')

        # Add text to the existing content
        updated_text = existing_text + "\nlambda success!"

        # Create the key for the processed file
        processed_key = object_key.replace("uploads/", "processed/", 1)

        # Upload the updated file to the processed folder
        s3.put_object(
            Bucket=bucket_name,
            Key=processed_key,
            Body=updated_text.encode('utf-8'),
            ContentType='text/plain'
        )

        print(f"Processed file uploaded to: {processed_key}")

    return {
        'body': json.dumps('Successfully processed S3 event!')
    }
