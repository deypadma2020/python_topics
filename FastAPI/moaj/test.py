from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Template

app = FastAPI()

# Mount static files (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Updated HTML Template with a modern design
html_template = Template('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="flex items-center justify-center h-screen bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-700">
    <div class="bg-white bg-opacity-10 backdrop-blur-xl p-8 rounded-2xl shadow-xl w-96 border border-white border-opacity-20">
        <h2 class="text-white text-4xl font-extrabold text-center mb-6">Welcome Back</h2>
        <p class="text-gray-200 text-center mb-4">Login to access your account</p>
        <form method="post" action="/login" class="space-y-4">
            <div>
                <input type="text" name="username" placeholder="Username" 
                       class="w-full p-3 rounded-lg bg-white bg-opacity-20 text-white placeholder-gray-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none" required>
            </div>
            <div>
                <input type="password" name="password" placeholder="Password" 
                       class="w-full p-3 rounded-lg bg-white bg-opacity-20 text-white placeholder-gray-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none" required>
            </div>
            <button type="submit" 
                    class="w-full bg-gradient-to-r from-indigo-500 to-purple-500 text-white py-3 rounded-lg font-semibold hover:opacity-80 transition shadow-lg">Login</button>
        </form>
        <p class="text-gray-300 text-center mt-4 text-sm">Forgot your password? <a href="#" class="text-indigo-300 hover:underline">Reset here</a></p>
    </div>
</body>
</html>
''')

@app.get("/", response_class=HTMLResponse)
def login_page():
    return html_template.render()

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "password":
        return RedirectResponse(url="/", status_code=303)
    return HTMLResponse(content="<h1 style='color:red; text-align:center;'>Invalid Credentials</h1>", status_code=401)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)