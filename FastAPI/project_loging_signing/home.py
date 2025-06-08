from fastapi.responses import HTMLResponse

async def get_home_page():
    with open("templates/home.html", "r") as f:
        return HTMLResponse(content=f.read())