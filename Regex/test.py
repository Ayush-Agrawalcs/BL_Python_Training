from abc import ABC,abstractmethod

class ATM:
    @abstractmethod
    def deposite():
        pass

class p(ATM):
    def deposite():
        print("deposite")

j=p()
p.deposite()