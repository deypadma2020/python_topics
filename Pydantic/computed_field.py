from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # m
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(
            (self.weight)/((self.height)**2)
        ,2)

        return bmi
    
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')

patient_info = {
    'name':'Suman', 
    'email':'abc@klizos.com', 
    'age': '30', 
    'weight': 75.2, 
    'height': 1.86,
    'married': True, 
    'allergies': ['pollen', 'dust'], 
    'contact_details':{'phone':'257097', 'emergency_contact': '9434342578'}
}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)