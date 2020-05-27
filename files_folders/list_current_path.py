import os

cwd = os.getcwd()  # Get the current working directory (cwd)

print("Path: %r" % (cwd))


files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

