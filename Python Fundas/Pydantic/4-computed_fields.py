from pydantic import BaseModel ,EmailStr ,AnyUrl , Field , field_validator , model_validator , computed_field
from typing import List, Dict,Optional ,Annotated 

class Patient(BaseModel):
    name: str
    email : EmailStr 
    Linkedin : AnyUrl
    age: int 
    weight: float
    height: float
    married : bool
    allergies : List[str]
    contact_details :Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float: 
        bmi_value = self.weight / ((self.height/100) ** 2)  # Assuming age is used as a proxy for height in meters
        return round(bmi_value, 2)


def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI:", patient.bmi)
    print("Inserted")

patient_info = {
    "name": "Shubham",
    "email": "shubham@hdfc.com",
    "Linkedin": "https://www.linkedin.com/in/shubham",
    "age": 70,
    "weight": 60.5,
    "height": 170,
    "married": False,
    "allergies": ["pollen", "dust"],
    "contact_details": {"phone": "123-456-7890","emergency": "098-765-4321"}
}

patient1 = Patient(**patient_info)

# Call the function
insert_patient(patient1)