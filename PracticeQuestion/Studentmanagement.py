class school:
    def __init__(self,school_name,student_id,name,age,marks,email):
        self.school_name=school_name
        self.student_id=student_id
        self.name=name
        self.age=age
        self.marks=marks
        self.email=email

class Student:
    def __init__(self):
        self.students={}
    
    def add_student(self,stu):
        if stu not in self.students:
            self.students[stu.student_id]=stu
        else:
            print("student already exist")
    
    def remove_student(self,stu_id):
        if stu_id in self.students:
            removed=self.students.pop(stu_id)
            print("this student is removed")
        else:
            print("Student not found")
    
    def update_marks(self,st_id,mark):
        if st_id in self.students:
            m=self.students[st_id]
            m.marks=mark
        else:
            print("student not found")
    
    def display(self):
        if not self.students:
            print("Student is Empty")
        else:
            for ab_name,st in self.students.items():
                   print(st.marks)

st=Student()
while(True):
    print("1 add student")
    print("2. remove student")
    print("3. display student")
    print("4. update marks")
    print("5. Extit")
    ch=int(input("Enter your Choice"))
    if ch==1:
        sc_name=input("Enter school name")
        st_id=input("Enter student id")
        name=input("Enter the name")
        age=input("Enter the age")
        marks=input("Enter the marks")
        email=input("Enter the email")
        st1=school(sc_name,st_id,name,age,marks,email)
        st.add_student(st1)
    elif ch==2:
        id=input("Enter the id")
        st.remove_student(id)
    elif ch==3:
        st.display()
    elif ch==4:
        id=input("Enter the id")
        mar=input("Enter the marks")
        st.update_marks(id,mar)
    elif ch==5:
        break
