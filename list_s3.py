import boto3

s3=boto3.client('s3')
response = s3.list_buckets()


'''print("Your S3 Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")'''

print("Your S3 buckets:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")