import os
# fastapi 붙여서 자동 프린터 서버 구축

filePath = './cache'
file_list = os.listdir(filePath)

for i in file_list:
    print(i)
    