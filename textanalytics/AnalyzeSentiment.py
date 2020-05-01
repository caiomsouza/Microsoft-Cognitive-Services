# Author: Caio Moreno

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
    "I did not like the restaurant. The food was too spicy.",
    "The restaurant was decorated beautifully. The atmosphere was unlike any other restaurant I've been to.",
    "The food was yummy. :)",
    """Custom speech provides tools that allow you to visually inspect the recognition quality of a model by comparing audio data with the corresponding recognition
 result from the custom speech portal. You can playback uploaded audio and determine if the provided recognition result is correct. 
 This tool allows you to quickly inspect quality of Microsoft's baseline speech to text model or a trained custom model without having to 
 transcribe any audio data.""",
 """Batman has the ability to function under great physical pain and withstand mind control. He is a master of disguise, multilingual and an expert in espionage, 
often gathering information under different identity's.""",
]

response = text_analytics_client.analyze_sentiment(documents, language="en")
result = [doc for doc in response if not doc.is_error]

for idx, doc in enumerate(result):
    print("Document text: {}\n".format(documents[idx]))
    print("Overall sentiment: {}".format(doc.sentiment))
    print("Scores: positive={}; neutral={}; negative={} \n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative,
))