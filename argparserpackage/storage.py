# This is for AWS backups to S3 with AWS CLI

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()  # streamed into file and closed

def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)

#>>> import boto3
#>>> from argparserpackage import storage
#>>> client = boto3.client('s3')
#>>> infile = open('example.txt', 'rb')
#>>> storage.s3(client, infile, 'python-developer', infile.name)

