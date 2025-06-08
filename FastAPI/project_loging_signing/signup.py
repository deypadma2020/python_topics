from fastapi import HTTPException, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
import json
import re

class SignupData(BaseModel):
    username: str
    email: str
    mobile: str
    password: str

def load_json():
    try:
        with open("signup_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_json(data):
    with open("signup_data.json", "w") as file:
        json.dump(data, file, indent=4)

def validate_field(field, field_type):
    if field_type == "email":
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, field):
            raise HTTPException(status_code=400, detail="Invalid email format")
    elif field_type == "mobile":
        if not (field.isdigit() and len(field) == 10):
            raise HTTPException(status_code=400, detail="Mobile must be 10 digits")
    elif field_type == "username":
        if not field.isalnum():
            raise HTTPException(status_code=400, detail="Username must be alphanumeric")

def validate_password(password):
    if len(password) <= 6:
        raise HTTPException(status_code=400, detail="Password must be more than 6 characters")
    if re.search(r"(.)\1{2,}", password) or re.search(r"123|234|345|456|567|678|789", password):
        raise HTTPException(status_code=400, detail="Password cannot have consecutive or repeated characters")

async def get_signup_page():
    with open("templates/signup.html", "r") as f:
        return HTMLResponse(content=f.read())

async def submit_signup(data: SignupData):
    signup_data = load_json()
    for entry in signup_data:
        if entry["username"] == data.username or entry["email"] == data.email or entry["mobile"] == data.mobile:
            raise HTTPException(status_code=400, detail="User already exists, please go to login")

    validate_field(data.username, "username")
    validate_field(data.email, "email")
    validate_field(data.mobile, "mobile")
    validate_password(data.password)

    new_entry = {"username": data.username, "email": data.email, "mobile": data.mobile, "password": data.password}
    signup_data.append(new_entry)
    save_json(signup_data)
    return RedirectResponse(url="/home", status_code=303)