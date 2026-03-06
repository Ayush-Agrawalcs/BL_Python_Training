class Student:
    name=""
    marks=0
    college_name="ABC College"
    def __init__(self,name,marks):
       self.name=name
       self.marks=marks

s1=Student("Ayush",87)
print(s1.name,s1.marks,s1.college_name)

s2=Student("Ankit",55)
print(s2.marks,s2.name)