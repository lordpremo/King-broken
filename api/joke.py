from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json, random, os

app = FastAPI(
    title="King Broken Comedy API",
    description="API yenye jokes nyingi sana 😂",
    version="2.0.0"
)

# Ruhusu CORS (hii ndiyo fix ya HTML yako)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ruhusu website yoyote
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JOKES_FILE = os.path.join(BASE_DIR, "jokes.json")

with open(JOKES_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
    jokes = data["jokes"]

@app.get("/")
def home():
    return {
        "message": "Karibu kwenye King Broken Comedy API 😂",
        "total_jokes": len(jokes),
        "endpoints": ["/joke", "/jokes"]
    }

@app.get("/joke")
def get_joke():
    return {"joke": random.choice(jokes)}

@app.get("/jokes")
def get_all_jokes():
    return {"count": len(jokes), "jokes": jokes}
