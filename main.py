from fastapi import FastAPI, Path, HTTPException, Query
import json

def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)

app = FastAPI()

@app.get("/")
def hello():
    return {'message': "Patient Management System"}

@app.get("/about")
def about():
    return {'message': "My name is Prakhar Dwivedi"}

@app.get("/view")
def view():
    return load_data()

@app.get("/patient/{id}")
def patient(
    id: str = Path(..., description="The ID of the patient to retrieve", example="pee1")
):
    data = load_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort(
    sort_by: str = Query(..., description="The field to sort by", example="weight"),
    order: str = Query("asc", description="The sort order (asc or desc)", example="asc")
):
    data = load_data()
    fields = ["weight", "gender", "height"]

    if sort_by not in fields:
        raise HTTPException(status_code=400, detail=f"select from {fields}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="choose asc/desc")

    reverse = (order == "desc")

    try:
        sorted_data = sorted(
            data.values(),
            key=lambda x: x[sort_by],
            reverse=reverse
        )
    except KeyError:
        raise HTTPException(status_code=400, detail=f"Some records missing '{sort_by}'")

    return sorted_data