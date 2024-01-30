# -*- coding: utf-8 -*-
from classes import BankAccount

trey_account = BankAccount(20)

print(trey_account.balance)
# 20

trey_account.deposit(100)
print(trey_account.balance)

# trey_account.balance
# 120

trey_account.withdraw(40)
print(trey_account.balance)

# trey_account.balance
# 80
print(trey_account)
# BankAccount(balance=80)

print(repr(trey_account))

mary_account = BankAccount(100)
print(mary_account.balance)

dana_account = BankAccount()
print(dana_account.balance)

mary_account.transfer(dana_account, 20)

print(mary_account.balance)
print(dana_account.balance)

print("Print all attributes")
print(trey_account.__dict__)
