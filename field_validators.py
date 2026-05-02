from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Optional


class Doctor(BaseModel):
    name: str
    email: EmailStr
    age: int
    link: AnyUrl

    @field_validator("email")
    @classmethod
    def email_validation(cls, val):
        domain = val.split("@")[-1]
        valid_domains = ["gmail.com", "iiitbhopal.ac.in"]

        if domain not in valid_domains:
            raise ValueError("Not supported email domain")

        return val


Doctor_data = {
    "name": "abcd",
    "age": 30,
    "email": "abcd@mail.com",
    "link": "https://linkedin.com/in/example"
}

Doctor1 = Doctor(**Doctor_data)


def insert_data(doctor: Doctor):
    print(doctor.name)
    print(doctor.age)


insert_data(Doctor1)