import os
import datetime
import shutil
import time
import server

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
    elif(action == "del"):
        file.write(f"[{time}]file {file_name} is deleted\n")
    elif(action == "Onserver"):
        file.write(f"[{time}]API SERVER : {file_name} server is On\n")
    else:
        file.write(f"[{time}]Request Error\n")
    file.close()
    return None

def PrintFile(file_list):
    file_Path = './cache'
    names = []
    for i in file_list:
        CopyFile(i)
        os.startfile(file_Path + "\\"+ i, "print")
        MakeLog("print", i)
        names.append(i)
    time.sleep(5)
    for j in names:
        DropFile(j)
        
def CopyFile(file_name):
    filePath = './cache'
    backup = './backup'
    shutil.copy(f'{filePath}//{file_name}', f'{backup}//{file_name}')
    MakeLog("copy", file_name)
    
def DropFile(file_name):
    filePath = './cache'
    os.remove(filePath + "//" + file_name)
    MakeLog("del", file_name)
        
if __name__ == "__main__":
    # PrintFile(GetFile())
    server.Runserver()