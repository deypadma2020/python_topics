def insert_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negetive")
        else:
            print(name)
            print(age)
            print("Data inserted")
    else:
        raise TypeError("Incorrect DataType")
    
def update_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Data updated")
    else:
        raise TypeError("Incorrect DataType")

insert_patient_data("Rajesh", 35)
insert_patient_data("Rajesh", '35')