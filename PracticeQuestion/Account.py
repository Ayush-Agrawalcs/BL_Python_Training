class Account:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.account_no=accountno
    
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")

    
    def get_balance(self):
        return self.balance


acc1=Account(1000,12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(500)
acc1.credit(400)
print(acc1.get_balance())