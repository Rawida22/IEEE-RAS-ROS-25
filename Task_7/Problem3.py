
class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance =balance
    def __Deposit__(self,amount):
        self.balance += amount
    def __Withdrawal__(self,amount):
        self.balance -= amount
    def bankFees(self):
        self.balance -= self.balance * 0.05
    def display(self):
        print(f"Account Number : {self.accountNumber}")
        print(f"Account Name : {self.name}")
        print(f"Account Balance : {int(self.balance)} $")


person1 = BankAccount(2178514584,'Ahmed',2952)
person1.__Deposit__(235)
person1.__Withdrawal__(450)
person1.bankFees()
person1.display()




        