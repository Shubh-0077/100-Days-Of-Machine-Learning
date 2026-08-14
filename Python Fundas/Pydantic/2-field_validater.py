from pydantic import BaseModel ,EmailStr ,AnyUrl , Field , field_validator
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

    @field_validator('email')
    @classmethod 
    def email_validator(cls, value):

        valid_domains = ["hdfc.com", "icici.com"] 

        domain = value.split('@')[-1] 
        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")         
        else :
            return value

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
    "age": 17,
    "weight": 60.5,
    "married": False,
    "allergies": ["pollen", "dust"],
    "contact_details": {"phone": "123-456-7890"}
}

patient1 = Patient(**patient_info)

# Call the function
insert_patient(patient1)