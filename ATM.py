class Atm:
    def __init__(self,cardnum,pin):
        self.cardnum = cardnum
        self.pin = pin
    def cashWithdrawl(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawn " + str(amount)+ ", Your reamining balance is " + str(new_amount))
    def balanceEnquiry(self):
        print("Your balance is " + 50000)

def main():
    cardnum = input("Enter Card Number: ")
    pin = input("Enter pin number: ")
    user = Atm(cardnum,pin)
    print("1.Balance Inquiry 2.Withdrawl")
    option = int(input("Choose your option: "))
    if(option == 1):
        user.balanceEnquiry()
    elif(option == 2):
        amount = int(input("Enter the amount: "))
        user.cashWithdrawl(amount)
    else:
        print("Enter a valid number")
main()