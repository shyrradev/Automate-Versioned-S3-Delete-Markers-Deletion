import boto3

bucket_name = 'my-bucket'
object_key = 'example.txt'

s3 = boto3.client('s3')

# List all versions of the object
versions = s3.list_object_versions(Bucket=bucket_name, Prefix=object_key)

# Delete all versions and delete markers
for version in versions.get('Versions', []) + versions.get('DeleteMarkers', []):
    version_id = version['VersionId']
    print(f'Deleting {object_key} version {version_id}')
    s3.delete_object(Bucket=bucket_name, Key=object_key, VersionId=version_id)

print(f'All versions and delete markers of {object_key} have been deleted.')
