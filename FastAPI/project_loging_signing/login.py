from fastapi import HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
import json

class LoginData(BaseModel):
    identifier: str  # username, email, or mobile
    password: str

def load_json():
    try:
        with open("signup_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

async def get_login_page():
    with open("templates/login.html", "r") as f:
        return HTMLResponse(content=f.read())

async def submit_login(data: LoginData):
    signup_data = load_json()
    for entry in signup_data:
        if (entry["username"] == data.identifier or entry["email"] == data.identifier or entry["mobile"] == data.identifier) and entry["password"] == data.password:
            return RedirectResponse(url="/home", status_code=303)
    raise HTTPException(status_code=400, detail="User not found or incorrect password, please sign up")