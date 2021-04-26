from secrets import access_key, secret_access_key
import os
import boto3 
 
s3    =   boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
for key in s3.list_objects(Bucket='hichambucket')['Contents']:
    
    if key['Key'].endswith('/'):
        if not os.path.exists('./'+key['Key']):
            os.makedirs('./'+key['Key'])
    else:
        print('key.name',key['Key'])
        s3.download_file('hichambucket', key['Key'],'./'+key['Key'])
