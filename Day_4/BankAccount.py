class BankAccount:
    def __init__(self,balance=0):
        self.__balance =balance
        
    def deposit(self,amt):
        self.__balance+=amt

    def withdraw(self,amt):
        if self.__balance>0:
            self.__balance-=amt
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    

acct = BankAccount()
acct.deposit(5000)
acct.withdraw(2000)
print(f"Final balance:{acct.get_balance()}")
# print(acct.balance) //error - cannot access balance as private var

