class Account:

    __last_account_number = 100
    def __init__(self,  hn, bal):
        print(self)
        self.__account_number = Account.__last_account_number+1
        Account.__last_account_number += 1
        self.__holders_name = hn
        self._balance = bal

    def deposit(self, amount):
        self._balance += amount 


    def withdraw(self, amount):
        self._balance -= amount    

 
    def print(self):
        print(f"Account {self.__account_number}, Holder {self.__holders_name}, balance {self._balance}")    


class SavingsAccount(Account): # how to override classes in Python
    
    def __init__(self, hn, balance, min_bal): # needed ONLY if you want to something in your own __init__
        super().__init__(hn,balance) # constructor chaining
        self.__min_bal = min_bal


    # override the base class behavior
    def withdraw(self, amount):
        if(self._balance - amount < self.__min_bal):
            print("Your poor guy.")
        else:
            self._balance -= amount

    # def print(self):        

# Allow us to withdraw MORE than what we have and the apply heavy interest
class CurrentAccount(Account):

    def __init__(self, hn, bal, cc_limit):
        print(self)
        super().__init__(hn, bal)
        self.cc_limit = cc_limit

    def withdraw(self, amount):
        print(self)
        if (amount > self._balance + self.cc_limit):
            print("you have exceeded your credit limit")
        else:
            self._balance -= amount

if False:
    acct = SavingsAccount("Google", 100000, 50000)
else:
    acct = CurrentAccount("Microsoft", 200000, 100000)         
acct.withdraw(3000000)
acct.print()            