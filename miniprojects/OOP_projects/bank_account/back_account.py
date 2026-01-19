
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, accountName,initialAmount= 0):
        self.balance = initialAmount
        self.account_name = accountName
        print(f"Account '{self.account_name}' created with initial balance: {self.balance}")    
        
    def get_balance(self):
        print(f"\nAccount name '{self.account_name}' balance: {self.balance:.2f}")
        return self.balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited {amount:.2f}. New balance: {self.balance:.2f}")
        
        
    def viable_transaction(self, amount):
        if amount > self.balance:
            raise BalanceException(f"Insufficient funds for withdrawal of {amount:.2f} from account {self.account_name}. Current balance: {self.balance:.2f}")
        else:
            return True
        
    def withdraw(self, amount):
        try:
            if self.viable_transaction(amount):   
                self.balance-= amount
                print(f"withdrew {amount:.2f}. New balanc: {self.balance:.2f}") 
                return self.balance
        except BalanceException as e:
            print(f"Withdrawal failed {e}") 

