import glob

location = 'C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services\\'


folderset = [folder for folder in glob.glob(location + "**/", recursive=True)]

for folder in folderset:
    print(folder)