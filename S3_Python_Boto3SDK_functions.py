import boto3

# Creates an S3 client
s3 = boto3.client('s3')
####################################################################

#function to create bucket and allow you to enter the name you want. 
def create_bucket():
    bucket_name = input("Enter the name of the bucket to create: ")
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
    print(f"Bucket {bucket_name} created.")
####################################################################
    
#function to list all buckets and print to screen
def list_buckets():
    response = s3.list_buckets()
    buckets = response['Buckets']
    print("All buckets:")
    for bucket in buckets:
        print(bucket['Name'])
####################################################################
       
#function to upload file and asks for the name of the file to upload. 
def upload_file(bucket_name):
    file_name = input("Enter the name of the file to upload: ")
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"File {file_name} uploaded to {bucket_name}.")
####################################################################

#function that lists all files in the bucket 
def list_files(bucket_name):
    response = s3.list_objects(Bucket=bucket_name)
    if 'Contents' in response:
        files = response['Contents']
        print(f"Files in {bucket_name}:")
        for file in files:
            print(file['Key'])
    else:
        print(f"No files in {bucket_name}.")
######################################################################

#function that deletes all files in the bucket
def delete_file(bucket_name):
    file_name = input("Enter the name of the file to delete: ")
    s3.delete_object(Bucket=bucket_name, Key=file_name)
    print(f"File {file_name} deleted.")
######################################################################

#function to delete bucket and asks you what is the name of the bucket you want to delete. 
def delete_bucket():
    bucket_name = input("Enter the name of the bucket to delete: ")
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted.")
######################################################################

#function to list the contents of the bucket and prompts for which file to read to to teh screen.  
def list_contents(bucket_name):
    file_name = input("Enter the name of the file to read: ")
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = obj['Body'].read().decode('utf-8')
    print(file_content)
######################################################################

#main function used to organize and call the order of the program
def main():
    # Create a bucket
    create_bucket()

    # List all buckets
    list_buckets()

    # Upload a file
    bucket_name = input("Enter the name of the bucket to use for upload: ")
    upload_file(bucket_name)

    # List all files in a particular bucket
    bucket_name = input("Enter the name of the bucket to list files from: ")
    list_files(bucket_name)

    # List the contents of the file that is in a bucket the bucket identified from the input
    bucket_name = input("Enter the name of the bucket the file is in you want to read: ")
    list_contents(bucket_name)

    # Delete a file
    bucket_name = input("Enter the name of the bucket to use for delete: ")
    delete_file(bucket_name)

    # Delete a bucket
    delete_bucket()
    
    

#calls main function to start program
main()