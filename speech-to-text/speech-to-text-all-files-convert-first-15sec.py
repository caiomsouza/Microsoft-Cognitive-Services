# Author: Caio Moreno

# Import Python Libraries
import glob
import azure.cognitiveservices.speech as speechsdk
import json

# Create a config file with your own configuration
# config_file_dev.json has my dev config
config_file_name = "speech-to-text/config_file/config_file_dev.json"

with open(config_file_name, 'r') as json_data_file:
    configuration = json.load(json_data_file)

print("################################")
#print(configuration)
print("################################")

speech_key = configuration["speech_api"]["speech_key"]
service_region = configuration["speech_api"]["service_region"]

#print("speech_key: " + speech_key)
print("service_region: " + service_region)


# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
speech_key, service_region = speech_key, service_region
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

print ("####################################################################################")
print ("PROGRAM START")
print ("####################################################################################")


# Function to convert audio files to text
def run_speech_to_text (file):
    print('Loading file...')
    print ("File: "+file)
    audio_filename = file
    audio_input = speechsdk.audio.AudioConfig(filename=audio_filename)

    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    result = speech_recognizer.recognize_once()
    print('Audio file content convert to text:')
    print('|')
    print(result)
    #result = speech_recognizer.recognize_once()
    print('|')
    return


# Define the files locations and list files
location = 'C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services\\speech-to-text\\data'
fileset = [file for file in glob.glob(location + "**/*.wav", recursive=True)]

# Loop to call function to convert audio files to text
for file in fileset:
    run_speech_to_text(file)
    print(file)

print ("END OF AUDIO FILES CONVERSION")