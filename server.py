import staticapi
import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "server is on"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    save_path = f"cache/{file.filename}"

    with open(save_path, "wb") as buffer:
        while True:
            chunk = await file.read(1024)
            if not chunk:
                break
            buffer.write(chunk)

    return {"filename": file.filename}

@app.get("/v1/print/{file_name}")
async def fileload(file_name):
    print(file_name)
    staticapi.PrintFile(file_name)
    return {"Message" : "print_requested"}

@app.get("/printall")
async def printall():
    staticapi.PrintFile(staticapi.GetFile())
    return {"Message" : "printingAll..."}

def Runserver():
    staticapi.MakeLog("Onserver", "fastapi")
    uvicorn.run(app, host="0.0.0.0", port=8000)