#classes and objects

class Student:
    #constructor
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll = roll
        self.marks =marks

    #method
    def display(self):
        print(f"Name:{self.name}\nRoll no:{self.roll}\nMarks: {self.marks}")

    
stu1 =Student("Harika",15,98)
print("Student 1 details: ")
stu1.display()

print()

stu2 =Student("Rishika",25,94)
print("Student 2 details: ")
stu2.display()


