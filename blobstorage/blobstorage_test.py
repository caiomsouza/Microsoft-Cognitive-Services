# Author: Caio Moreno

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import json
import os

cwd = os.getcwd()  # Get the current working directory (cwd)

print ("################################################################")
print("Path: %r" % (cwd))
print ("################################################################")
print ("################################################################")

files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
print ("################################################################")
print ("################################################################")
print ("################################################################")


# Create a config file with your own configuration
# config_file_dev.json has my dev config
# config_file_name = "../../blobstorage/config_file/config_file_dev.json"
config_file_name = "blobstorage/config_file/config_file_dev.json"


with open(config_file_name, 'r') as json_data_file:
    configuration = json.load(json_data_file)

print("################################")
#print(configuration)
print("################################")

# Blob Storage
connect_str = configuration["blob_storage"]["connect_str"]
local_folder_full_path = configuration["local_folder"]["local_folder_full_path"]

print("Blob Connection String: " + connect_str)    
print("Local folder path:  " + local_folder_full_path)   

container_name_initials = "blob-demo-caio"


try:
    print("Azure Blob storage v12 - Python quickstart sample")
    print(connect_str)

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = container_name_initials + str(uuid.uuid4())

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    ## Upload blobs to a container
    ## https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-quickstart-blobs-python#upload-blobs-to-a-container

    # Create a file in local data directory to upload and download
    local_path = "./"
    local_file_name = "caio-demo-file" + str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    file = open(upload_file_path, 'w')
    file.write("Caio Demo")
    file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

    ## List the blobs in a container
    ## https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-quickstart-blobs-python#list-the-blobs-in-a-container

    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

    ## Download blobs
    ## https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-quickstart-blobs-python#download-blobs

    # Download the blob to a local file
    # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    ## Delete a container
    ## https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-quickstart-blobs-python#delete-a-container

    # Clean up
    print("\nPress the Enter key to begin clean up")
    input()

    print("Deleting blob container...")
    container_client.delete_container()

    print("Deleting the local source and downloaded files...")
    os.remove(upload_file_path)
    os.remove(download_file_path)

    print("Done")


except Exception as ex:
    print('Exception:')
    print(ex)