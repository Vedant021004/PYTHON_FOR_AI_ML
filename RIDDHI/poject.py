# maek the ATM machine which accept the user input 
# 1. pin , 2. balance , 3.withdraw, 4.deposit
# pin should be type int and private, balance also private
# hint --> balance -= withdraw .........
# try and except for example ---> "invalid user", "invalid amount"

class Bank:
    def __init__(self,balance = 0, pin = 1234):
        self.__balance = balance
        self.pin = pin

    def withdraw(self,amount):
        self.amount = amount 

        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrawn {amount} succesfully")

        else:
            print("insufficient balance")

    def depositt(self,deposit):
        self.deposit = deposit

        self.__balance += deposit    
        print(f"your amount {deposit} succesfully deposited")

    def show_balance(self):

        return self.__balance

obj = Bank()    


while True:
    pin = int(input("please enter teh pin:  "))

    if pin == 1234:

        print("you loggedin succsfylly")

        
        user = int(input("PLEASE ENTER THE OPTIONS:"
        "1. check balance : "
        "2. withdraw : "
        "3. deposit : "))


        if user == 1:
            print("your current balance is:", obj.show_balance())

        elif user == 2:
            withdraww = int(input("please enter the amount you want to withdraw"))
            obj.withdraw(withdraww)    

        elif user == 3:
            amount = int(input("please enter the amount you wan tto deposit"))
            obj.depositt(amount)

        else:
            print("incorrect option")

    else:
        print("incorrect pin")          


