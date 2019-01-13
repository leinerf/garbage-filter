import boto3

def sendImageToBucket(file_name):
    s3 = boto3.client('s3',
            aws_access_key_id="change this",
            aws_secret_access_key="change this")
    bucket = 'sbhacksv-garbage-collector'
    file_name = 'plastic.jpeg'
    key_name = 'plastic1.jpeg'
    s3.upload_file(file_name, bucket, key_name)
    return file_name