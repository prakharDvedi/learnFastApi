from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return { 'message': "Namaste"}

@app.get("/about")
def about():
    return { 'message': "My name is Prakhar Dwivedi"}