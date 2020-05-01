# Author: Caio Moreno
# pip install <please install all azure python libs before your run this code>

# This was removed from the latest lib (azure-ai-textanalytics 1.0.0b4)
# https://pypi.org/project/azure-ai-textanalytics/
# https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/textanalytics/azure-ai-textanalytics/samples/sample_recognize_pii_entities.py
# https://pypi.org/project/azure-ai-textanalytics/

# Need to use version azure-ai-textanalytics 1.0.0b3 for this feature
# https://pypi.org/project/azure-ai-textanalytics/1.0.0b3/#recognize-pii-entities


from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import json

# Create a config file with your own configuration
# config_file_dev.json has my dev config
config_file_name = "../textanalytics/config_file/config_file_dev.json"

with open(config_file_name, 'r') as json_data_file:
    configuration = json.load(json_data_file)

print("################################")
#print(configuration)
print("################################")

credential = configuration["text_api"]["credential"]
endpoint = configuration["text_api"]["endpoint"]

#print("credential: " + credential)
print("endpoint: " + endpoint)

# Text API 
credential = AzureKeyCredential(credential)
endpoint = endpoint

text_analytics_client = TextAnalyticsClient(endpoint, credential)

documents = [
    "The employee's SSN is 555-55-5555.",
    "The employee's phone number is 555-55-5555.",
    "My mobile phone is +44 7722 263641"
]

response = text_analytics_client.recognize_pii_entities(documents, language="en")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    for entity in doc.entities:
        print("Entity: \t", entity.text, "\tType: \t", entity.type,
              "\tConfidence Score: \t", entity.score)
