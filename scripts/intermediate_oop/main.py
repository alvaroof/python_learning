# -*- coding: utf-8 -*-
from classes import BankAccount
from properties import Circle

trey_account = BankAccount(20)

print(trey_account._balance)
# 20

trey_account.deposit(100)
print(trey_account._balance)

# trey_account.balance
# 120

trey_account.withdraw(40)
print(trey_account._balance)

# trey_account.balance
# 80
print(trey_account)
# BankAccount(balance=80)

print(repr(trey_account))

mary_account = BankAccount(100)
print(mary_account._balance)

dana_account = BankAccount()
print(dana_account._balance)

mary_account.transfer(dana_account, 20)

print(mary_account._balance)
print(dana_account._balance)

print("Print all attributes")
print(trey_account.__dict__)

my_account = BankAccount(10)

my_account.deposit(100)

my_account.withdraw(40)

my_account.deposit(95)

print(my_account.transactions)
[("OPEN", 10, 10), ("DEPOSIT", 100, 110), ("WITHDRAWAL", -40, 70), ("DEPOSIT", 95, 165)]

circle = Circle()

print(circle.radius)
print(circle.diameter)
print(circle.area)

circle.radius = 10
print(circle.radius)
print(circle.diameter)
print(circle.area)

circle.diameter = 10
print(circle.radius)
print(circle.diameter)
print(circle.area)

print(mary_account > dana_account)

