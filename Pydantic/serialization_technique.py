from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: int
    country: str

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {
    'city': 'Bethuadahari',
    'state': 'West Bengal',
    'pin': '741126',
    'country': 'India'
}
address1 = Address(**address_dict)

patient_dict ={
    'name': 'Deb',
    # 'gender': 'Male',
    'age': 26,
    'address': address1 # address_dict
}
patient = Patient(**patient_dict)

temp = patient.model_dump()

print(temp)
print(type(temp))
print("-----------------------------------------\n")

temp = patient.model_dump()

print(temp)
print(type(temp))
print("-----------------------------------------\n")

temp = patient.model_dump_json()

print(temp)
print(type(temp))
print("-----------------------------------------\n")

temp = patient.model_dump(exclude=['name', 'address'])

print(temp)
print(type(temp))
print("-----------------------------------------\n")

temp = patient.model_dump(exclude_unset=True)

print(temp)
print(type(temp))
print("-----------------------------------------\n")

temp = patient.model_dump(exclude_defaults=True)

print(temp)
print(type(temp))
print("-----------------------------------------\n")

temp = patient.model_dump(exclude={'address': ['state']})

print(temp)
print(type(temp))
print("-----------------------------------------\n")

temp = patient.model_dump(exclude={'name': True, 'address': {'state': True}})

print(temp)
print(type(temp))
print("-----------------------------------------\n")