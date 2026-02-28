from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Data model
class Affirmation(BaseModel):
    text: str
    mood: str
    favorite: bool = False

# Temporary storage
affirmations = []

@app.get("/")
def home():
    return {"message": "Daily Affirmations API is running 💖"}

# Add affirmation
@app.post("/affirmations")
def add_affirmation(affirmation: Affirmation):
    affirmations.append(affirmation)
    return {"message": "Affirmation added ✨"}

# Get all affirmations
@app.get("/affirmations")
def get_all():
    return affirmations

# Get random affirmation
@app.get("/affirmations/random")
def get_random():
    if not affirmations:
        return {"message": "No affirmations yet 💭"}
    return random.choice(affirmations)