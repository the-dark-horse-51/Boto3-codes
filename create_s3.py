import boto3

#creating an s3 client to interact with the s3 bucket service
s3 = boto3.client('s3')

#set a globally unique bucket name
bucket_name = 'abduss-bucket-2341'

#create bucket in a specific region
region = 'us-east-1'

'''s3.create_bucket(Bucket = bucket_name)
print(f'Bucket - {bucket_name} created successfully!')'''

try:
    if region == 'us-east-1':
        s3.create_bucket(Bucket = bucket_name)
    else:
        s3.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration ={'LocationConstraint':region}
        )

    print(f"✅ Bucket '{bucket_name}' created successfully!")
except Exception as e:
    print(f"❌ Error: {e}")