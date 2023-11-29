import os

filePath = './cache'
file_list = os.listdir(filePath)

for i in file_list:
    print(i)
    