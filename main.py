from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AIAMBU backend running"}
@app.post("/request_ambulance")
def request_ambulance():
    return {
        "status": "searching",
        "message": "Searching nearest hospital ambulance..."
    }
