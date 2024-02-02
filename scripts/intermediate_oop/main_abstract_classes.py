from classes import BankAccount
import abc

class MinimumBankAccount(BankAccount):
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Can't withdraw {amount} (balance is €{self._balance})")
        super().withdraw(amount)
        
class Duck(abc.ABC):
    @abc.abstractmethod
    def quack(self):
        pass
    
class Goose(Duck):
    def quack(self):
        print("Quack")


if __name__ == '__main__':
    account = MinimumBankAccount(10)
    try:
        account.withdraw(100)
    except:
        account.withdraw(5)
        print(account.balance)
    print(account)
    
    goose = Goose()
    goose.quack()