import boto
from boto.s3.key import Key
import sys

AWS_ACCESS_KEY_ID = 'AKIA************6V'
AWS_SECRET_ACCESS_KEY = 'hA************************6t'
END_POINT = 'ca-central-1'
S3_HOST = 's3.ca-central-1.amazonaws.com'
BUCKET_NAME = 'lightrez-bucket'        
FILENAME = sys.argv[1]

s3 = boto.s3.connect_to_region(END_POINT,
                           aws_access_key_id=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                           host=S3_HOST)

bucket = s3.get_bucket(BUCKET_NAME)
k = Key(bucket)
k.key = FILENAME
k.set_contents_from_filename(FILENAME)