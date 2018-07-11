# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:37:06 2018

@author: caio.f.moreno
"""

# https://docs.microsoft.com/en-gb/azure/cognitive-services/text-analytics/quickstarts/python


import requests
from pprint import pprint

# change the subscription key for your own subscription_key
subscription_key = '<your_subscription_key>'
text_analytics_base_url = 'https://westeurope.api.cognitive.microsoft.com/text/analytics/v2.0/' 
sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)



documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'},
  {'id': '5', 'language': 'en', 'text': 'This is pretty cool that now we can have a car'}
]}


headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)

