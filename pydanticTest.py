from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

patient_data = {'name': "abcd", 'age': '30'}

patient1 = Patient(**patient_data)

def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)

insert_data(patient1)