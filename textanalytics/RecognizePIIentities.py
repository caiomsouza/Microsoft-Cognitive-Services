from azure.ai.textanalytics import TextAnalyticsClient

credential = "YOUR_KEY"
endpoint = "https://westeurope.api.cognitive.microsoft.com/"
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