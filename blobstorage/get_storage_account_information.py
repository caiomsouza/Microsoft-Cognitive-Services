# Author: Caio Moreno
# Based on this code https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/storage/azure-storage-blob/samples/blob_samples_service.py

## Import Libs
import os
from azure.core.exceptions import ResourceNotFoundError, ResourceExistsError
from azure.storage.blob import BlobServiceClient
from azure.mgmt.resource import ResourceManagementClient
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


# Instantiate a BlobServiceClient using a connection string
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

def get_storage_account_information():
    # [START get_blob_service_account_info]
    account_info = blob_service_client.get_account_information()
    print('Using Storage SKU: {}'.format(account_info['sku_name']))
    # [END get_blob_service_account_info]

    # [START get_blob_service_stats]
    stats = blob_service_client.get_service_stats()
    # [END get_blob_service_stats]
    print(stats)


def list_all_containers():
    # List all containers
    all_containers = blob_service_client.list_containers(include_metadata=True)
    for container in all_containers:
        print(container['name'], container['metadata'])


## Call the Function to give Blob Storage details
get_storage_account_information()
## Call the Function to List all containers
list_all_containers()