import os
from pathlib import Path
import azure.cognitiveservices.speech as speechsdk

speech_key = "YOUR_KEY"
service_region = "YOUR_REGION"
#service_region = "uksouth"

# audio2.wav
audio_file_path = Path("C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services\\speech-to-text\\data\\audio2.wav").resolve()

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_input = speechsdk.AudioConfig(filename=str(audio_file_path))
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

def recognize_audio_file():
    print('Recognizing first result...')

    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print('Recognized: {}'.format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print('No speech could be recognized: {}'.format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print('Speech Recognition canceled: {}'.format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print('Error details: {}'.format(cancellation_details.error_details))

if __name__ == '__main__':
    recognize_audio_file()


#audio1.wav
#audio_file_path = Path("C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services\\speech-to-text\\data\\audio1.wav").resolve()

#batman
#audio_file_path = Path("C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services\\speech-to-text\\data\\batman.wav").resolve()
