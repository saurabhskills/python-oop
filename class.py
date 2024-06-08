class Student:
    # class attribute
    name =""
    age=0

# creating object of class Student
Saurabh = Student()
Saurabh.name = "Saurabh Kumar Yadav"
Saurabh.age = 20

Deepak = Student()
Deepak.name = "Deepak Kumar"
Deepak.age = 21

# access the class object information
print(f"{Saurabh.name} is {Saurabh.age} years old.")
