from fastapi import FastAPI
import json


def load_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data
app = FastAPI()

@app.get("/")
def hello():
    return { 'message': "Patient Management System"}

@app.get("/about")
def about():
    return { 'message': "My name is Prakhar Dwivedi"}


@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/patient/{id}")
def patient(id: str):
    data = load_data()
    if id in data:
        return data[id]
    return { 'message': "Patient not found"}
