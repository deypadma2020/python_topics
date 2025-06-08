from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import json
import re
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Define a model for the login data
class LoginData(BaseModel):
    identifier: str  # username, email, or mobile
    password: str

# Load or create login_data.json
def load_json():
    try:
        with open("login_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_json(data):
    with open("login_data.json", "w") as file:
        json.dump(data, file, indent=4)

# Validation function for consecutive or repeated characters
def is_consecutive(s):
    print(f"Checking identifier: {s}")
    # Check for three or more repeated characters (e.g., "aaa")
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            print(f"Rejected: Three or more repeats '{s[i]}{s[i + 1]}{s[i + 2]}' at position {i}")
            return True
    # Check for consecutive numbers (e.g., "123")
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isdigit():
            if int(s[i + 1]) == int(s[i]) + 1:
                print(f"Rejected: Consecutive numbers '{s[i]}{s[i + 1]}' at position {i}")
                return True
    # Check for consecutive letters (e.g., "abc")
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i + 1].isalpha():
            if ord(s[i].lower()) + 1 == ord(s[i + 1].lower()):
                print(f"Rejected: Consecutive letters '{s[i]}{s[i + 1]}' at position {i}")
                return True
    print("Accepted: No issues found")
    return False

# Validate identifier format
def validate_identifier(identifier):
    print(f"Validating identifier: {identifier}")
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if "@" in identifier and re.match(email_pattern, identifier):
        print("Identifier is an email")
        return "email"
    elif identifier.isdigit() and len(identifier) == 10:
        print("Identifier is a mobile number")
        return "mobile"
    elif identifier.isalnum():
        print("Identifier is a username")
        return "username"
    else:
        print("Invalid identifier format")
        raise HTTPException(status_code=400, detail="Invalid identifier format")

# Validate password
def validate_password(password):
    if len(password) <= 6:
        raise HTTPException(status_code=400, detail="Password must be more than 6 characters")
    if is_consecutive(password):
        raise HTTPException(status_code=400, detail="Password cannot have consecutive or repeated characters")

# Serve the login page
@app.get("/", response_class=HTMLResponse)
async def get_login_page():
    with open("login.html", "r") as f:
        return f.read()

# Handle login submission
@app.post("/login")
async def submit_login(data: LoginData):
    print(f"Received identifier: {data.identifier}, password: {data.password}")
    identifier_type = validate_identifier(data.identifier)
    if is_consecutive(data.identifier):
        raise HTTPException(status_code=400, detail="Identifier cannot have consecutive or repeated characters")
    validate_password(data.password)
    login_data = load_json()
    for entry in login_data:
        if entry["identifier"] == data.identifier:
            raise HTTPException(status_code=400, detail="User already exists in our database")
    new_entry = {"identifier": data.identifier, "password": data.password, "type": identifier_type}
    login_data.append(new_entry)
    save_json(login_data)
    return {"message": "Login successful! Welcome to the home page."}

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081, reload=True)