class Account:

    __last_account_number = 100
    def __init__(self,  hn, bal):
        self.__account_number = Account.__last_account_number+1
        Account.__last_account_number += 1
        self.__holders_name = hn
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount 


    def withdraw(self, amount):
        self.__balance -= amount    

    def __eq__(self, other):
        return self.__balance == other.__balance 

    def __gt__(self, other):
        return self.__balance > other.__balance 

    def __lt__(self, other):
        return self.__balance < other.__balance 

    def __ge__(self, other):
        return self.__balance >= other.__balance

    def __le__(self, other):
        return self.__balance <= other.__balance 


    def __ne__(self, other):
        return self.__balance != other.__balance 





    def print(self):
        print(f"Account {self.__account_number}, Holder {self.__holders_name}, balance {self.__balance}")    

acct = Account("Guido van Rossum", 200000)
acct.print()
dacct = Account("Nitin", 200000)
dacct.print()

if acct < dacct:
    print("Nitin is rich")
else:
    print("Guido is rich")    

if acct > dacct:
    print("Guido is rich")
else:
    print("Nitin is rich")

if acct == dacct:
    print("Both are rich")

if acct != dacct:
    print("Both have different amount of money")


print(acct.__dict__)
print(acct._Account__balance)

# acct.print()

# a = 0
# if a := False:
#     print("yes")
# else:
#     print("no") 


# def f(x):
#     return x**2
# x = 2
# test = [y := f(x), y**2, y**3]
# print(test)    
