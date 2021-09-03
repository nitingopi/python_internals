from Account import Account
class SavingsAccount(Account): # how to override classes in Python
    
    def __init__(self, hn, balance, min_bal): # needed ONLY if you want to something in your own __init__
        super().__init__(hn,balance) # constructor chaining
        self.__min_bal = min_bal


    # override the base class behavior
    def withdraw(self, amount):
        if(self._balance - amount < self.__min_bal):
            # print("Your poor guy.")
            raise Exception("Your poor guy")
        else:
            self._balance -= amount