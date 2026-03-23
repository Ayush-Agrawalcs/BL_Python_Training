class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    @property
    def get_sal(self):
        return self.__salary
    @get_sal.setter
    def set_sal(self,sal):
       self.__salary=sal
    
    def calculated(self):
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculated(self):
        bonus=self.get_sal+self.get_sal*0.2
        self.set_sal=bonus
        return self.get_sal
    
# class Developer(Employee):
#     dict={}
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
    
#     def calculated(self):
#         self.salary=self.salary+self.salary*0.1
#         dict[self.name]=self.salary
#         return self.salary

m=Manager("Ayush",80000)
print(m.calculated())

# d=Developer("Ankur",50000)
# print(d.calculated())

# list=[m,d]

