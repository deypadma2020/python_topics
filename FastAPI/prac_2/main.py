from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'message': 'Hello World'}

@app.get('/about')
def about():
    return {'message': 'hey! I just started to learn about FastAPI'}

