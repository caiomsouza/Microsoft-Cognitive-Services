# Author: Caio Moreno
# pip install <please install all azure python libs before your run this code>

from azure.ai.textanalytics import single_analyze_sentiment

def score_sentiment_analysis(endpoint, credential, input_text):

    response = single_analyze_sentiment(endpoint=endpoint, credential=credential, input_text=input_text)
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.3f}; neutral={1:.3f}; negative={2:.3f} \n".format(
        response.document_scores.positive,
        response.document_scores.neutral,
        response.document_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("[Offset: {}, Length: {}]".format(sentence.offset, sentence.length))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.3f}\nNeutral={1:.3f}\nNegative={2:.3f}\n".format(
            sentence.sentence_scores.positive,
            sentence.sentence_scores.neutral,
            sentence.sentence_scores.negative,
        ))


credential = "YOUR_KEY"
endpoint = "https://westeurope.api.cognitive.microsoft.com/"
# document = "I had the best day of my life. I wish you were there with me."
input_text = "Politics as we know it is changing - not just in America and Britain but across the continent of Europe too, where new and often right wing parties, led by charismatic populists, have been springing up and winning votes."

score_sentiment_analysis(endpoint, credential, input_text)
print ("No Loop")


texts = ['I had the best day of my life. I wish you were there with me.',
          'I love London, but I hate the rain',
          'Not to bad this day of my life. I wish you were there with me.',
          'I had the worst day of my life. I wish you were there with me.']

for index in range(len(texts)):
    score_sentiment_analysis(endpoint, credential, texts[index])
print ("Good bye!")
