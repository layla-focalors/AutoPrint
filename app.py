import os
import datetime
import shutil

def GetFile():
    filePath = './cache'
    file_list = os.listdir(filePath)
    return file_list

def MakeLog(action, file_name):
    time = datetime.datetime.now()
    file = open("log.txt", "a")
    if(action == "print"):
        file.write(f"[{time}]file {file_name} is printed\n")
    elif(action == "copy"):
        file.write(f"[{time}]file {file_name} is backuped\n")
    file.close()
    return None

def PrintFile(file_list):
    file_Path = './cache'
    for i in file_list:
        CopyFile(i)
        os.startfile(file_Path + "\\"+ i, "print")
        MakeLog("print", i)
        
def CopyFile(file_name):
    filePath = './cache'
    backup = './backup'
    shutil.copy(f'{filePath}//{file_name}', f'{backup}//{file_name}')
    MakeLog("copy", file_name)
        
if __name__ == "__main__":
    PrintFile(GetFile())