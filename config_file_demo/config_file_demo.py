import json

config_file_name = "../config_file_demo/config_file_demo.json"

with open(config_file_name, 'r') as json_data_file:
    configuration = json.load(json_data_file)

print("################################")
print(configuration)
print("################################")

speech_key = configuration["speech_api"]["speech_key"]
service_region = configuration["speech_api"]["service_region"]

print("speech_key: " + speech_key)
print("service_region: " + service_region)