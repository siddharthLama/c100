class Atm(object):
    def __init__(self,cardNo,pin) :
        self.CardNo = cardNo
        self.pin = pin
        self.balance = 100000

    def checkBalance(self):
        print(self.balance)

    def cashWithdrawl(self,amount):
        self.balance = self.balance - amount
        print("withrawl sucessfull and your balance is ",self.balance)

def main():
    cardNo = input("input your cad number :-")
    pin = input("input your pin :-")
    newUser = Atm(cardNo,pin)
    print("choose your activity")
    print("1.balanceEnquire 2.cash withdrawl")    
    activity = int(input("enter your activity :-"))
    if activity == 1 : 
        newUser.checkBalance()
    elif activity == 2 : 
        amount = int(input("enter the amount"))
        
        newUser.cashWithdrawl(amount)
    else: 
        print("enter a valid number")

main()
