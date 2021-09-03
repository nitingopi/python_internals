from Account import Account

class CurrentAccount(Account):

    def __init__(self, hn, bal, cc_limit):
        # print(self)
        super().__init__(hn, bal)
        self.cc_limit = cc_limit

    def withdraw(self, amount):
        # print(self)
        if (amount > self._balance + self.cc_limit):
            print("you have exceeded your credit limit")
        else:
            self._balance -= amount