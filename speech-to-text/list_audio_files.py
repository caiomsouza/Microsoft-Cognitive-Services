# Author: Caio Moreno 

# Import lib
import glob

print ("START ###################################################################")

# Function 
def list_audio_files (file):
    print ("File: "+file)
    return

# Config your audio files location
location = 'C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services\\speech-to-text\\data'
fileset = [file for file in glob.glob(location + "**/*.wav", recursive=True)]

# Loop to list audio files
for file in fileset:
    list_audio_files(file)
    print(file)

print ("END ###################################################################")