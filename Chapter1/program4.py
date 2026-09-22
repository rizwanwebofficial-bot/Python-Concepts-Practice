import os

path = "C:\\Users\\Dell\\Documents"   # Change to your directory path

contents = os.listdir(path)

for item in contents:
    print(item)