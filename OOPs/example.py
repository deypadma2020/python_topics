# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def Display(self):
#         print(self.name, self.marks)

#     def Change_data(self):
#         self.name = input('Enter your name: ')
#         self.marks = int(input('Enter your marks: '))

###########################################################################

# std1 = Student('Riya', 98)
# std2 = Student('Manta', 89)
# std3 = Student('Stuti', 88)

# print(std2.__dict__)

# std2.Change_data()
# print(std2.__dict__)

########################################################################

# class NegetiveAge(Exception):
#     pass

# class Age:
#     def __init__(self, age):
#         if age<0:
#             raise NegetiveAge("Age can't be negetive")
#     def __del__(self):
#         print("Destructure is called")

# age = Age(-10)

##########################################################################

# class Employee:
#     def __init__(self, first, last):
#         self.first_name = first
#         self.last_name = last
#         # self.mail = first.lower() + last.lower() + '@jcm.com'

#     @property
#     def mail(self):
#         return f'{self.first_name.lower()}{self.last_name.lower()}@jcm.com'

#     @property
#     def full_name(self): #getter method
#         return f"{self.first_name} {self.last_name}"
    
#     @full_name.setter
#     def full_name(self, name): #setter method
#         first, last = name.split()
#         self.first_name = first
#         self.last_name = last

#     @full_name.deleter
#     def full_name(self):
#         self.first_name = None
#         self.last_name = None
    
# e = Employee('Souvik', 'Dey')
# e1 = Employee('Soukarjya', 'Sanphui')
# e2 = Employee('Sougata', 'Dutta')

# e.first_name = 'x'
# print(e.first_name)
# print(e.last_name)
# print(e.mail)
# print(e.full_name)
# e.last_name = 'y'
# e.full_name = 'Ultimate Crazy'
# print(e.full_name)

# del e.full_name
# print(e.full_name)

##################################################################################################

stack = []

class Stack:
    def __init__(self, homepage):
        self.stack = [homepage]

    # this function will going to check whether the stack is empty
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    # function for getting stack's top element    
    def get_top(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.stack[-1]

    # function for push operation(append / insert)    
    def push(self, ele):
        self.stack.append(ele)

    # function for pop operation
    def stack_pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            print("can't delete")
        else:
            deleted_ele = self.stack.pop()
            print(deleted_ele, "got_deleted")
            if not self.isEmpty():
                print("Redirected to - ", self.get_top())

    # display all elements from stack / history
    def display(self):
        x = len(self.stack)
        for i in range(x-1, -1, -1):
            print(self.stack[i])

    # function for checking length of stack
    def length(self):
        return len(self.stack)
    


links_stack = Stack('home.html')

while True:
    print('-' * 60)
    choice = int(input("Please enter the last choice\n1. Visit another link - \n2. Back\n3. History\n4. Gets latest visited place\n5. Close the Browser\n"))
    print('-' * 60)

    if choice ==1:
        link = input('Enter the link - ')
        links_stack.push(link)
    elif choice == 2:
        links_stack.stack_pop()
    elif choice == 3:
        links_stack.display()
    elif choice == 4:
        latest_visited = links_stack.get_top()
        print("Latest visited link - ", latest_visited)
    elif choice == 5:
        break
    else:
        print("Invalid choice")

    if links_stack.isEmpty():
        break


########################################################################################

# # need of property decorator
# class Employee:
#     def __init__(self, first, last):
#         self.firstname = first
#         self.lastname = last
#         # self.mail = first+last+"@gmail.com"

#     @property
#     def mail(self):
#         return f"{self.firstname+self.lastname}@gmail.com"

#     def fullname(self):
#         return f"{self.firstname} {self.lastname}"
    
# e = Employee("priya", "basak")
# e1 = Employee("sunny", "giri")
# e2 = Employee("manisha", "ghosh")

# e.firstname = "Jay"

# print(e.firstname)
# print(e.mail)
# print(e.fullname())
# print("-"*50)

# print(e1.firstname)
# print(e1.mail)
# print(e1.fullname())
# print("-"*50)

# print(e2.firstname)
# print(e2.mail)
# print(e2.fullname())

# e.fullname = "Dipankar Biswas"


#######################################################################################

# # need of property decorator
# class Employee:
#     def __init__(self, first, last):
#         self.firstname = first
#         self.lastname = last
#         # self.mail = first+last+"@gmail.com"

#     @property
#     def mail(self):
#         return f"{self.firstname}{self.lastname}@gmail.com"

#     @property
#     def fullname(self):  #getter method
#         return f"{self.firstname} {self.lastname}"
    
#     @fullname.setter
#     def fullname(self, name):  #setter method
#         first, last = name.split()
#         self.firstname = first
#         self.lastname = last

#     @fullname.deleter
#     def fullname(self):  #deleter method
#         self.firstname = None
#         self.lastname = None
    
# e = Employee("priya", "basak")
# e1 = Employee("sunny", "giri")
# e2 = Employee("manisha", "ghosh")

# e.firstname = "Jay"

# print(e.firstname)
# print(e.mail)

# e.fullname = "Dipankar Biswas"

# print("---- After using setter method----")
# print(e.firstname)
# print(e.lastname)
# print(e.fullname)
# print(e.mail)

# del e.fullname
# print("---- After using deleter method ----")
# print(e.firstname)
# print(e.lastname)
# print(e.fullname)
# print(e.mail)
