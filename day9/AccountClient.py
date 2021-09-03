from CurrentAccount import CurrentAccount
from SavingsAccount import SavingsAccount

sa = SavingsAccount("Bill Gates", 100000, 10000)
sa.print()

ca = CurrentAccount("Elon Musk", 20000, 5000)
ca.print()

try:
    sa.withdraw(100000)
except Exception as e:
    print(e.args[0])    

try:
    ca.withdraw(30000)    
except Exception as e:
    print(e.args[0])     