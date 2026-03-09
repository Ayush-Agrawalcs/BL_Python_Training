class Student:
    name=""
    roll_number=0
    marks=0

    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
        

    def display_details(self):
        print(self.name , self.roll_number, self.marks)

    def calculate_grade(self):
        if(self.marks>=90):
            return 'A'
        elif self.marks>75:
            return 'B'
        elif self.marks>=50:
            return 'C'
        else:
            return "Fail"


k=Student("Ayush",2215500040,90)
k.display_details()
print(k.calculate_grade())