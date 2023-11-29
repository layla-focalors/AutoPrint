import os
import datetime

def GetFile():
    filePath = './cache'
    file_list = os.listdir(filePath)
    return file_list

def MakeLog(action, file_name):
    file = open("log.txt", "a")
    if(action == "print"):
        time = datetime.datetime.now()
        file.write(f"[{time}]file {file_name} is printed\n")
    file.close()
    return None

def PrintFile(file_list):
    file_Path = './cache'
    for i in file_list:
        os.startfile(file_Path + "\\"+ i, "print")
        MakeLog("print", i)
        
if __name__ == "__main__":
    PrintFile(GetFile())