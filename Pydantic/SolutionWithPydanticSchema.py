from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
print("------------------------------------------")

# def insert_patient_data(name: str, age: int):
#     print(name)
#     print(age)
#     print("Data Inserted")

def insert_patient_data(patient_info: Patient):
    print(patient_info.name)
    print(patient_info.age)
    print("Data Inserted")

patient_info = {
    'name': 'Ross',
    'age': 40
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)
print("------------------------------------------")

def update_patient_data(patient_info: Patient):
    print(patient_info.name)
    print(patient_info.age)
    print("Data Updated")

patient_info = {
    'name': 'Rose',
    'age': '45'
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
print("------------------------------------------")


def update_patient_data(patient_info: Patient):
    print(patient_info.name)
    print(patient_info.age)
    print("Data Updated")

patient_info = {
    'name': 'Rose',
    'age': 'Forty five'
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
print("------------------------------------------")
