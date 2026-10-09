from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def display(self):
        pass

class Account(Bank):
    def __init__(self):
        self.__balance = 10000

    def display(self):
        print("Balance:", self.__balance)

a = Account()
a.display()
