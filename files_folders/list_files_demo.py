import glob
import os

location = 'C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services\\speech-to-text\\data'

fileset = [file for file in glob.glob(location + "**/*.wav", recursive=True)]

for file in fileset:
    print(file)

print ("###################################################################")

location2 = 'C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services'


# List Python files
for file in os.listdir(location2):
    if file.endswith(".py"):
        print(os.path.join(location2, file))


print ("###################################################################")




location3 = 'C:\\Users\\camoren\\Documents\\GitHub\\Microsoft-Cognitive-Services'

files_in_dir = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(location3):
   for item in f:
      if '.txt' in item:
         files_in_dir.append(os.path.join(r, item))

for item in files_in_dir:
   print("file in dir: ", item)


print ("###################################################################")




p = r"C:\Users\camoren\Documents\GitHub\Microsoft-Cognitive-Services\speech-to-text\data\batman.wav"


# Get the filename only from the initial file path.
filename = os.path.basename(p)

# Use splitext() to get filename and extension separately.
(file, ext) = os.path.splitext(filename)

# Print outcome.
print("Filename without extension =", file)
print("Extension =", ext)


