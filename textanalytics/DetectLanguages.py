# Author: Caio Moreno
# pip install <please install all azure python libs before your run this code>

# pip install azure-ai-textanalytics

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
       "This document is written in English.",
       "Il documento scritto in italiano.",
       "Este es un document escrito en Español.",
       "Este documento esta escrito em..",
       "这是一个用中文写的文件",
       "Dies ist ein Dokument in deutsche Sprache.",
       "Detta är ett dokument skrivet på engelska."
   ]


response = text_analytics_client.detect_language(documents)
result = [doc for doc in response if not doc.is_error]

for idx, doc in enumerate(result):
       if not doc.is_error:
           print("Document text: {}".format(documents[idx]))
           print("Language detected: {}".format(doc.primary_language.name))
           print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
           print("Confidence score: {}\n".format(doc.primary_language.score))
       if doc.is_error:
           print(doc.id, doc.error)