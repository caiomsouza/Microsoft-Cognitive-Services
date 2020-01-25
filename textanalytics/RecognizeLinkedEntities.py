from azure.ai.textanalytics import TextAnalyticsClient

credential = "YOUR_KEY"
endpoint = "https://westeurope.api.cognitive.microsoft.com/"

text_analytics_client = TextAnalyticsClient(endpoint, credential)


documents = [
    "Microsoft was founded by Bill Gates and Paul Allen.",
    "Easter Island, a Chilean territory, is a remote volcanic island in Polynesia.",
    "Caio Moreno is a Cloud Solution Architect at Microsoft UK",
    "I love London"
]

response = text_analytics_client.recognize_linked_entities(documents, language="en")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    for entity in doc.entities:
        print("Entity: {}".format(entity.name))
        print("Url: {}".format(entity.url))
        print("Data Source: {}".format(entity.data_source))
        for match in entity.matches:
            print("Score: {0:.3f}".format(match.score))
            print("Offset: {}".format(match.offset))
            print("Length: {}\n".format(match.length))