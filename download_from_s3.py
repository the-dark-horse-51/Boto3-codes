import boto3

s3 = boto3.client('s3')

bucket_name = 'abduss-bucket-2341'
object_name = 'uploaded_sample_file.txt'
download_path = 'downloaded_sample_file.txt'

try:
    s3.download_file(bucket_name, object_name, download_path)
    print(f'File {object_name} downloaded successfully from {bucket_name}')
except Exception as e:
    print(f"Error: {e}")

    
