# Author: Caio Moreno
# pip install <please install all azure python libs before your run this code>

from azure.ai.textanalytics import TextAnalyticsClient

credential = "YOUR_KEY"
endpoint = "https://westeurope.api.cognitive.microsoft.com/"

text_analytics_client = TextAnalyticsClient(endpoint, credential)

documents = [
    "Redmond is a city in King County, Washington, United States, located 15 miles east of Seattle.",
    "I need to take my cat to the veterinarian.",
    "I will travel to South America in the summer."
]

response = text_analytics_client.extract_key_phrases(documents, language="en")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    print(doc.key_phrases)
