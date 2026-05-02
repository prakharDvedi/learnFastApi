from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List, Dict, Optional, Annotated

# annotated lets us Off type coercion, add description and details to the input along with constraints

class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            title="Name of the patient",
            description="The name of the patient in less than 50 chars",
            examples=["Nitish", "Amit"],
            max_length=50
        )
    ]

    email: EmailStr
    linkedin_url: AnyUrl

    age: Annotated[int, Field(gt=0, lt=90)]

    weight: Annotated[float, Field(gt=0, strict=True)]

    married: Annotated[
        Optional[bool],
        Field(default=None, description="Is the patient married or not")
    ]

    allergies: Annotated[
        Optional[List[str]],
        Field(default=None, max_length=5)
    ]

    contact_details: Dict[str, str]

patient_data = {'name': "abcd", 'age': '30'}

patient1 = Patient(**patient_data)

def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)

insert_data(patient1)