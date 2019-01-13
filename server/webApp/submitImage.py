import boto3

def sendImageToBucket(file_name):
    s3 = boto3.client('s3',
            aws_access_key_id="secret_key",
            aws_secret_access_key="secret_access_key")
    bucket = 'sbhacksv-garbage-collector'
    key_name = 'photo.jpg'
    s3.upload_file(file_name, bucket, key_name)
    return file_name