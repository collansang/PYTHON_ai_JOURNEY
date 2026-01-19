from back_account import *

collo = BankAccount("TiropArapBengat", 1200)
mary = BankAccount("Mary")

collo.get_balance()
collo.deposit(500)
mary.get_balance()

collo.withdraw(300)
mary.withdraw(100)