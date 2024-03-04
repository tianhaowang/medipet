import boto3
import sys
from botocore.exceptions import NoCredentialsError
import uuid  # Import the UUID library
import os 
# Constants for AWS access
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = 'medibottian'

# Initialize the S3 client
s3 = boto3.client('s3', 
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  region_name='us-east-2')

def configure_aws_credentials():
    # Configure AWS credentials
    boto3.setup_default_session(aws_access_key_id=AWS_ACCESS_KEY_ID, 
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def upload_file_to_s3(object_name, local_file_path, folder):
    # Generate a unique object name using UUID
    unique_object_name = f"{uuid.uuid4()}_{object_name}"
    full_object_name = f"{folder}/{unique_object_name}"
    s3.upload_file(local_file_path, BUCKET_NAME, full_object_name, ExtraArgs={'ACL':'public-read'})
    # Create the S3 URL after uploading
    file_url = f"https://{BUCKET_NAME}.s3.us-east-2.amazonaws.com/{full_object_name}"
    print("File uploaded to: ", file_url)
    return file_url

def upload_request_to_s3(file, original_object_name, folder):
    # Generate a unique object name using UUID
    unique_object_name = f"{uuid.uuid4()}_{original_object_name}"
    full_object_name = f"{folder}/{unique_object_name}"

    try:
        # Instead of saving the file locally, upload it directly to S3
        s3.upload_fileobj(file, BUCKET_NAME, full_object_name, ExtraArgs={'ACL': 'public-read'})

        # Create the S3 URL after uploading
        file_url = f"https://{BUCKET_NAME}.s3.us-east-2.amazonaws.com/{full_object_name}"
        print("File uploaded to: ", file_url)
        return file_url
    
    except Exception as e:
        print("Something went wrong: ", e)
        return None

def delete_object_from_s3_by_url(file_url):
    # Extract the object name from the URL
    # Assuming the URL format is "https://[bucket-name].s3.[region].amazonaws.com/[folder]/[object_name]"
    path_parts = file_url.split(f"https://{BUCKET_NAME}.s3.us-east-2.amazonaws.com/")
    if len(path_parts) < 2:
        print("Invalid S3 URL")
        return False
    
    object_name = path_parts[1]  # The part after the bucket URL

    try:
        # Use the delete_object method to remove the object from the bucket
        s3.delete_object(Bucket=BUCKET_NAME, Key=object_name)
        print(f"File {object_name} deleted from bucket {BUCKET_NAME}")
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except Exception as e:
        print(f"Something went wrong: {e}")
        return False
    
def download_file_from_s3(object_name, local_file_path):
    s3.download_file(BUCKET_NAME, object_name, local_file_path)

def list_objects_in_bucket():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    # Print the object keys
    for obj in response.get('Contents', []):  # Check if 'Contents' exists to avoid KeyError
        print(obj['Key'])

def delete_object_from_bucket(object_name):
    s3.delete_object(Bucket=BUCKET_NAME, Key=object_name)

if __name__ == "__main__":
    configure_aws_credentials()

    # Collect arguments from the command line
    if len(sys.argv)  == 0:
        print("Usage: python3 storage.py <file_name> <object_name> <local_file_path>")
        sys.exit(1)

    object_name = sys.argv[1]
    local_file_path = sys.argv[2]
    folder = sys.argv[3]

    # Perform the S3 operations
    upload_file_to_s3(object_name, local_file_path, folder)
    
    # Uncomment below functions as needed and provide appropriate arguments
    # download_file_from_s3(object_name, local_file_path)
    # list_objects_in_bucket()
    # delete_object_from_bucket(object_name)
