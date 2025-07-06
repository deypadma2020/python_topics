from pydantic import BaseModel, EmailStr, AnyUrl,Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length=50)
    age: int = Field(gt=0,lt=150)
    weight: float
    email: EmailStr
    linkedin: AnyUrl
    married: Optional[bool] = False
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]

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
