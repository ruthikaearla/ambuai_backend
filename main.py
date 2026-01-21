from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

# 1️⃣ Home endpoint
@app.get("/")
def home():
    return {"message": "AIAMBU backend running"}

# 2️⃣ Request ambulance endpoint
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

# 3️⃣ Simulated ambulances (keep this near top, after endpoints is fine too)
ambulances = [
    {"id": 1, "lat": 22.56, "lon": 88.36, "status": "available"},
    {"id": 2, "lat": 22.57, "lon": 88.37, "status": "available"},
]

# 4️⃣ New endpoint for live ambulance tracking — add **after the ambulances list**
@app.get("/ambulance_locations")
def get_ambulance_locations():
    """
    Returns all current ambulance locations
    """
    return {"status": "success", "ambulances": ambulances}
