from fastapi import FastAPI
import uvicorn
from signup import get_signup_page, submit_signup, SignupData
from login import get_login_page, submit_login, LoginData
from home import get_home_page

app = FastAPI()

# Signup routes
app.get("/")(get_signup_page)
app.post("/signup")(submit_signup)

# Login routes
app.get("/login")(get_login_page)
app.post("/login")(submit_login)

# Home route
app.get("/home")(get_home_page)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8081, reload=True)

# uvicorn main:app --reload --port 8081