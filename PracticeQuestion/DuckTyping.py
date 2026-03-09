class Bird:
    def fly(self):
        print("Bird flying")


class Aeroplane:
    def fly(self):
        print("Aeroplane flying")

def flying(a):
    a.fly()

a=Bird()
b=Aeroplane()

flying(a)
# flying(b)
