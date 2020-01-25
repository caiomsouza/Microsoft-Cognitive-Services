from azure.ai.textanalytics import TextAnalyticsClient

credential = "YOUR_KEY"
endpoint = "https://westeurope.api.cognitive.microsoft.com/"

text_analytics_client = TextAnalyticsClient(endpoint, credential)

documents = [
    "This is written in English.",
    "Il documento scritto in italiano.",
    "Dies ist in englischer Sprache verfasst.",
    "Este documento esta escrito en..",
    "Este documento esta escrito em.."
]

response = text_analytics_client.detect_languages(documents)
result = [doc for doc in response if not doc.is_error]

for doc in result:
    print("Language detected: {}".format(doc.primary_language.name))
    print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
    print("Confidence score: {}\n".format(doc.primary_language.score))