from pydantic import BaseModel ,EmailStr ,AnyUrl , Field , field_validator , model_validator
from typing import List, Dict,Optional ,Annotated 

class Patient(BaseModel):
    name: str
    email : EmailStr 
    Linkedin : AnyUrl
    age: int 
    weight: float
    married : bool
    allergies : List[str]
    contact_details :Dict[str,str]

    @model_validator(mode='after')
    def val_eme_con(cls, model): 
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old.")
        return model

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted")

patient_info = {
    "name": "Shubham",
    "email": "shubham@hdfc.com",
    "Linkedin": "https://www.linkedin.com/in/shubham",
    "age": 70,
    "weight": 60.5,
    "married": False,
    "allergies": ["pollen", "dust"],
    "contact_details": {"phone": "123-456-7890","emergency": "098-765-4321"}
}

patient1 = Patient(**patient_info)

# Call the function
insert_patient(patient1)