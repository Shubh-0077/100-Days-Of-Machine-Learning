from pydantic import BaseModel ,EmailStr ,AnyUrl , Field
from typing import List, Dict,Optional ,Annotated 

# ========================= Pydantic Imports Reference =========================
# BaseModel        -> Base class for creating data models with automatic
#                     validation, type checking, and serialization.

# EmailStr         -> Validates that a field contains a valid email address.
#                     Example: "user@example.com"

# AnyUrl           -> Validates that a field contains a valid URL.
#                     Supports HTTP, HTTPS, FTP, etc.

# Field            -> Adds extra validation and metadata to model fields.
#                     Used for constraints like gt, ge, lt, default values,
#                     descriptions, examples, aliases, etc.

# field_validator  -> Validates or modifies a single field before/after
#                     model creation.
#                     Used for custom validation logic.

# model_validator  -> Validates the entire model.
#                     Useful when validation depends on multiple fields.

# computed_field   -> Creates a calculated field that is generated from
#                     other fields and is included in the model output.
#                     No need to store it separately.

# ========================= Typing Imports Reference =========================
# List             -> Represents a list of items of the same type.
#                     Example: List[str]

# Dict             -> Represents a dictionary with key-value types.
#                     Example: Dict[str, int]

# Optional         -> Field can either contain a value or None.
#                     Equivalent to: str | None

# Annotated        -> Adds extra metadata or validation rules to a type.
#                     Commonly used with Field() in Pydantic.
#                     Example: Annotated[int, Field(gt=0)]
# ===========================================================================


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name" , description="Name of the patient", example=["Shubham", "Tina"])]
    email : EmailStr 
    Linkedin : Optional[AnyUrl]
    age: int 
    weight: Annotated[float, Field(gt=0, lt=120 , strict = True)]
    married : Annotated[bool, Field(default=False, description="Marital status of the patient")]
    allergies : Annotated[Optional[List[str]], Field(default=None, max_length=5)] 
    contact_details :Dict[str,str]

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
    "email": "shubham@example.com",
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