# method overriding
class Payment:
    def pay(self,amount):
        print("Payment processed")

class  CreditCard(Payment):
    def pay(self,amount):
        print("Paid", amount, "using Credit Card")


class Paypal(Payment):
    def pay(self, amount):
        print("Paid", amount, "using PayPal")

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")
        
p1 = CreditCard()
p2 = Paypal()
p3 = UPI()

p1.pay(1000)
p2.pay(2000)
p3.pay(500)