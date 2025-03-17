import boto3

#create an s3 client
s3 = boto3.client('s3')

bucket_name = 'abduss-bucket-2341'
file_name = 'sample.txt'
object_name = 'uploaded_sample_file.txt'

try:
    #upload the file
    s3.upload_file(file_name, bucket_name, object_name)
    print(f'✅ File "{file_name}" uploaded to "{bucket_name}/{object_name}" successfully!')
except Exception as e:
    print(f"Error: {e}")

