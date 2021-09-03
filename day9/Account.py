class Account:

    __last_account_number = 100
    def __init__(self,  hn, bal):
        # print(self)
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
