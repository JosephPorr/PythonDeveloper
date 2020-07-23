# This is for local backups

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()  # streamed into file and closed

def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)
