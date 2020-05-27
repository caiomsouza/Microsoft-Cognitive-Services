# Speech to Text Demo using Microsoft Azure Cognitive Services SDK
This demo will show how to use the Microsoft Azure Cognitive Services to convert audio files (.wav format) to text. <BR>

Example audio files are located in the [data folder](https://github.com/caiomsouza/Microsoft-Cognitive-Services/tree/master/speech-to-text/data)<BR>

## Install library
```
pip install azure-cognitiveservices-speech
```

# Script to convert all audio files (small or large audio files) to CSV output (Recommened Script)
```
python speech-to-text-all-files_large_files_parse_result_save_to_csv.py > script_output.log
```

# Other Scripts

### Code to convert all audio files (small or large audio files) in the folder and save text to .log file
```
python speech-to-text-all-files_large_files.py > output/output_all_content_audio_files_20200501_01.log
```

### Code to list all audio files in the folder
```
python "list_audio_files.py
```

### Code to convert the first 15 seconds of all audio files in the folder and save text to .log file
```
python speech-to-text-all-files_large_files.py > output/output_audio_files_first_15sec_20200501_01.log
```

### Tool to convert M4a audio files to wav audio files
https://www.zamzar.com/convert/m4a-to-wav/

### Reference
https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/quickstart/python/from-microphone
