# Author: Caio Moreno
# pip install <please install all azure python libs before your run this code>

from azure.ai.textanalytics import TextAnalyticsClient

credential = "YOUR_KEY"
endpoint = "https://westeurope.api.cognitive.microsoft.com/"

text_analytics_client = TextAnalyticsClient(endpoint, credential)

documents = [
    "Microsoft was founded by Bill Gates and Paul Allen.",
    "Redmond is a city in King County, Washington, United States, located 15 miles east of Seattle.",
    "Jeff bought three dozen eggs because there was a 50% discount."
]

response = text_analytics_client.recognize_entities(documents, language="en")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    for entity in doc.entities:
        print("Entity: \t", entity.text, "\tType: \t", entity.type,
              "\tConfidence Score: \t", entity.score)


