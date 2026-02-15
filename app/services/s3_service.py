import boto3, uuid, os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET = os.getenv("AWS_BUCKET_NAME")

def upload_file(file):
    filename = f"{uuid.uuid4()}_{file.filename}"
    s3.upload_fileobj(file.file, BUCKET, filename)
    return f"https://{BUCKET}.s3.amazonaws.com/{filename}"
