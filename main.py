from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AIAMBU backend running"}
@app.post("/request_ambulance")
async def request_ambulance(request: Request):
    data = await request.json()  # parse JSON body

    patient_name = data.get("patient_name")
    location = data.get("location")
    
    if not patient_name or not location:
        raise HTTPException(status_code=400, detail="Missing patient_name or location")
    
    return {
        "status": "searching",
        "message": "Searching nearest hospital ambulance..."
    }

