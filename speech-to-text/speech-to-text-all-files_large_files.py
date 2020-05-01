# Author: Caio Moreno 


# Code to save the output to a file
# python "speech-to-text-all-files_large_files.py" > output_speech_to_text_20200501_01.log

# Import Python Libraries
import glob
import azure.cognitiveservices.speech as speechsdk
import time
import json

# Create a config file with your own configuration
# config_file_dev.json has my dev config
config_file_name = "../speech-to-text/config_file/config_file_dev.json"

with open(config_file_name, 'r') as json_data_file:
    configuration = json.load(json_data_file)

print("################################")
#print(configuration)
print("################################")

# Speech SDK
speech_key = configuration["speech_api"]["speech_key"]
service_region = configuration["speech_api"]["service_region"]

# File location
location = configuration["location"]["full_file_path"]

#print("speech_key: " + speech_key)
print("service_region: " + service_region)


# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
speech_key, service_region = speech_key, service_region
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

print ("####################################################################################")
print ("PROGRAM START")
print ("####################################################################################")

# Function to convert large audio files (15 seconds only) to text
def speech_recognize_continuous_from_file(file):

    print('Loading file...')
    print ("File: "+file)
    print ("####################################################################################")

    """performs continuous speech recognition with input from an audio file"""
    # <SpeechContinuousRecognitionWithFile>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(filename=file)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    done = False

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)

    speech_recognizer.stop_continuous_recognition()
    # </SpeechContinuousRecognitionWithFile>

    print ("Audio File: "+file+" converted successfully")
    print ("####################################################################################")


# Define the files locations and list audio files (*.wav)
#location = 'C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services\\speech-to-text\\data'
location = location

fileset = [file for file in glob.glob(location + "**/*.wav", recursive=True)]

# Loop to call function to convert audio files to text
for file in fileset:
    #run_speech_to_text_small_audio_files(file)
    speech_recognize_continuous_from_file(file)
    print(file)

print ("####################################################################################")
print ("PROGRAM END")
print ("####################################################################################")
print ("Thank you for using this code")