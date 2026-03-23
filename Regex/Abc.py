class A:
    def __init__(self,shoes_id,name):
        self.name=name
        self.shoes_id=shoes_id
    
    def display(self):
        print(self.shoes_id,self.name)
class B:
    def __init__(self,name,shoe_id):
        self.name=name
        self.shoe_id=shoe_id
    
    def display(self):
        print(self.name,self.shoe_id)

class C:
    def __init__(self):
        self.add_shoes=[]
        self.add_users=[]
        self.booked={}
    
    def add_shoe(self,A):
        for c in self.add_shoes:
            if c.shoes_id==A.shoes_id:
                print("Shoes already in stock")
                return
        self.add_shoes.append(A)
    
    def display(self):
        for con in self.add_shoes:
            con.display()
            print("---------")
    
    def add_user(self,B):
        for b in self.add_users:
            if(b.shoe_id==B.shoe_id):
                print("user exist")
                return
        self.add_users.append(B)
    
    def display_user(self):
        for con in self.add_users:
            con.display()
            print("---------")
    
    def book_shoes(self):
        for a in self.add_shoes:
            for b in self.add_users:
                if(a.shoes_id==b.shoe_id):
                    self.booked[b.shoe_id]=a.name,b.name
        print(self.booked)
    def prin(self):
        for id, (name, na) in self.booked.items():
            print(id, name, na)

    

c=C()
a=A(1,"campus")
b=A(1,"Addidas")
c.add_shoe(a)

c.add_shoe(b)
c.display()
d=B("Ayush",1)
e=B("Ayush",1)
c.add_user(d)
c.add_user(e)
c.display_user()
c.book_shoes()
c.prin()
