import random


class BankAccount():
    def __init__(self):
        self.savingsAccount = {}

    def createAccount(self, name, depositAmount):
        self.accountNumber = random.randint(11111,99999)
        self.savingsAccount[self.accountNumber] = [name, depositAmount]
        print("\nAccount Created for ", name)
        print("\nAccount number: ",self.accountNumber)
        self.displayBalance()

    def validateAccount(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if name == self.savingsAccount[accountNumber][0]:
                print("\nUser authenticated\n")
                self.accountNumber = accountNumber
                return True
            else:
                print("\nAuthentication failed\n")
                return False
        else:
            print("\nAuthentication failed\n")
            return False

    def deposit(self,depositAmount):
        self.savingsAccount[self.accountNumber][1]+=depositAmount
        self.displayBalance()

    def withdraw(self,withdrawAmount):
        if withdrawAmount < self.savingsAccount[self.accountNumber][1]:
            self.savingsAccount[self.accountNumber][1]-=withdrawAmount
        else:
            print("\nInsufficient Balance\n")
        self.displayBalance()

    def displayBalance(self):
        print("\nAvailable Balance: ",self.savingsAccount[self.accountNumber][1])


def main():
    account = BankAccount()
    print("\n","*"*10,"Welcome to ABC Bank","*"*10,"\n")
    while True:
        print("\n1 Create Account")
        print("2 Access existing account")
        print("3 Exit\n")
        userChoice = int(input())
        if userChoice == 1:
            print("Enter Name")
            name=input()
            print("Enter initial deposit amount")
            deposit=int(input())
            account.createAccount(name,deposit)
        elif userChoice == 2:
            print("Enter Name")
            name = input()
            print("Enter Account Number")
            accountNumber = int(input())
            val=account.validateAccount(name,accountNumber)
            if val:
                while True:
                    print("\n1 Deposit Amount\n2 Withdraw Amount\n3 Check Balance in Account\n4 Go back to previous Menu\n")
                    choice=int(input())
                    if choice == 1:
                        deposit=int(input("Enter deposit amount: "))
                        account.deposit(deposit)
                    elif choice == 2:
                        withdraw=int(input("Enter withdrawal amount: "))
                        account.withdraw(withdraw)
                    elif choice == 3:
                        account.displayBalance()
                    else:
                        break
        else:
            break


main()