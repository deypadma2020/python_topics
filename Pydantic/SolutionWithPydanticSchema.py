from pydantic import BaseModel, EmailStr, StrictInt, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str = Field(max_length=50)
    age: int = Field(gt=0,lt=150)
    weight: Annotated[float, Field(gt=0, strict=True)]
    email: Annotated[EmailStr, Field(title='Email of the Patient', description="Provide a valid email id", examples=['padma.dey@empeal.com', 'padma@klizos.com'])]
    linkedin: AnyUrl
    phone_no: Annotated[Optional[StrictInt], Field(max_digits=10)]
    married: Optional[bool] = False
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=10, description="It's an optional field")]
    contact_details: Optional[Dict[str, str]]

patient_info = {
    'name': 'Ross',
    'age': -40, # negetive value
    'weight': 50.7,
    'email': "abcgmail.com", # @ missing
    'linkedin': "://linkedin.com/ross2025", # https missing
    # 'married': True,
    'allergies': ['Dust', 'Apple', 'Banana'],
    'contact_details': {'email': "abc@gmail.com", 'phone_no': '9434342578'}

}
print("------------------------------------------")

# def insert_patient_data(name: str, age: int):
#     print(name)
#     print(age)
#     print("Data Inserted")

def insert_patient_data(patient_info: Patient):
    print(patient_info.name)
    print(patient_info.age)
    print(patient_info.contact_details)
    print("Data Inserted")

patient1 = Patient(**patient_info)
insert_patient_data(patient1)
print("------------------------------------------")

# def update_patient_data(patient_info: Patient):
#     print(patient_info.name)
#     print(patient_info.age)
#     print("Data Updated")

# patient_info = {
#     'name': 'Rose',
#     'age': '45'
# }

# patient1 = Patient(**patient_info)
# update_patient_data(patient1)
# print("------------------------------------------")


# def update_patient_data(patient_info: Patient):
#     print(patient_info.name)
#     print(patient_info.age)
#     print("Data Updated")

# patient_info = {
#     'name': 'Rose',
#     'age': 'Forty five'
# }

# patient1 = Patient(**patient_info)
# update_patient_data(patient1)
# print("------------------------------------------")
