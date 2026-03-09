class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num):
        real=self.real+num.real
        img=self.img+num.img
        return Complex(real,img)
    
    def __sub__(self,num):
        real=self.real-num.real
        img=self.img-num.img
        return Complex(real,img)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

result=num1+num2
result.showNumber()

result1=num1-num2
result1.showNumber()