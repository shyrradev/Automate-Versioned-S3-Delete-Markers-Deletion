# Automate-Versioned-S3-Delete-Markers-Deletion
Overview
This script demonstrates how to delete all versions and delete markers of a specific object in an Amazon S3 bucket using the boto3 library. This is particularly useful for managing versioned objects in your S3 bucket.

Prerequisites
Python 3.x
boto3 library
AWS credentials configured (using AWS CLI or by setting environment variables)
Setup
Install boto3:

If you don't already have boto3 installed, you can install it using pip:

bash
Copy code
pip install boto3
Configure AWS Credentials:

Ensure that your AWS credentials are configured. You can set them up using the AWS CLI:

bash
Copy code
aws configure
Alternatively, you can set the following environment variables:

bash
Copy code
export AWS_ACCESS_KEY_ID='your-access-key-id'
export AWS_SECRET_ACCESS_KEY='your-secret-access-key'
export AWS_DEFAULT_REGION='your-region'
Script Explanation
The script performs the following steps:

Initialize the S3 client:

python
Copy code
s3 = boto3.client('s3')
List all versions of the specified object:

python
Copy code
versions = s3.list_object_versions(Bucket=bucket_name, Prefix=object_key)
Delete all versions and delete markers:

The script iterates over all versions and delete markers of the object and deletes them one by one.

python
Copy code
for version in versions.get('Versions', []) + versions.get('DeleteMarkers', []):
    version_id = version['VersionId']
    print(f'Deleting {object_key} version {version_id}')
    s3.delete_object(Bucket=bucket_name, Key=object_key, VersionId=version_id)
Print confirmation:

Once all versions and delete markers are deleted, the script prints a confirmation message.

python
Copy code
print(f'All versions and delete markers of {object_key} have been deleted.')
Usage
Set the bucket name and object key:

Update the bucket_name and object_key variables with the appropriate values for your S3 bucket and object.

python
Copy code
bucket_name = 'my-bucket'
object_key = 'example.txt'
Run the script:

Execute the script using Python:

bash
Copy code
python delete_s3_object_versions.py
Ensure that your AWS credentials and permissions allow you to list and delete object versions in the specified S3 bucket.

Notes
This script will permanently delete all versions and delete markers of the specified object. Use it with caution.
Ensure you have the necessary permissions to delete objects in the S3 bucket.
Troubleshooting
Permission errors: Ensure that your AWS credentials have the necessary permissions to list and delete object versions in the specified S3 bucket.
Configuration errors: Verify that your AWS credentials and region are correctly configured.
