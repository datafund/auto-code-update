import boto3
from dotenv import load_dotenv
import argparse
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os

load_dotenv()

def upload_file_to_s3(file_path, bucket_name, object_name=None, region_name='us-east-1', expiration=3600):
    """
    Upload a file to an S3 bucket and generate a presigned URL.

    :param file_path: Path to the ZIP file to upload.
    :param bucket_name: Name of the S3 bucket.
    :param object_name: S3 object name (if None, file_path name is used).
    :param region_name: AWS region of the bucket.
    :param expiration: Time in seconds for the presigned URL to remain valid (default: 3600 seconds).
    :return: Presigned URL of the uploaded file.
    """
    # Use the file name if object_name is not specified
    if object_name is None:
        object_name = os.path.basename(file_path)

    # Create an S3 client
    s3_client = boto3.client('s3', region_name=region_name)

    try:
        # Upload the file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to S3 bucket '{bucket_name}' as '{object_name}'.")

        # Generate a presigned URL for the uploaded file
        presigned_url = s3_client.generate_presigned_url('get_object',
                                                         Params={'Bucket': bucket_name, 'Key': object_name},
                                                         ExpiresIn=expiration)
        print("Presigned URL:", presigned_url)
        return presigned_url

    except FileNotFoundError:
        print("Error: The file was not found.")
    except NoCredentialsError:
        print("Error: AWS credentials not available.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials provided.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None


def main():
    parser = argparse.ArgumentParser(description="Uploads a file to AWS S3 and returns a presigned URL of the file.")
    parser.add_argument('bucket', type=str, help="S3 bucket name")
    parser.add_argument('file_path', type=str, help="Path of the file to be uploaded")
    
    args = parser.parse_args()
    bucket = args.bucket
    file_path = args.file_path

    presigned_url = upload_file_to_s3(file_path, bucket)
    if presigned_url:
        print("Access your file using this presigned URL:")
        print(presigned_url)

if __name__ == "__main__":
    main()


    
