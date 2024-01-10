# -*- coding: utf-8 -*-
from prettytable import PrettyTable


class Requirement:
    water = 20
    coffee = 5
    milk = 20
    money = 2


class MachineException(Exception):
    pass


class Machine:
    operating = True

    def __init__(self) -> None:
        self.water = 100
        self.milk = 50
        self.coffee = 76
        self.money = 2.5

    @staticmethod
    def prompt():
        return input("What would you like? (espresso/latte/cappuccino/): ")

    def turn_off(self):
        print("Deactivating machine...")

    def print_report(self):
        table = PrettyTable()
        table.add_column("Object", ["Water", "Milk", "Coffee", "Money"])
        table.add_column("Amount", [self.water, self.milk, self.coffee, self.money])
        table.add_column("Unit", ["ml", "ml", "g", "$"])
        print(table)

    def make_coffee(self):
        print("Making coffee...")
        self.water -= Requirement.water
        self.milk -= Requirement.milk
        self.coffee -= Requirement.coffee
        self.money -= Requirement.money
        input("Please take your coffee.")

    def validate_resources(self):
        return (
            (self.water > Requirement.water)
            & (self.coffee > Requirement.coffee)
            & (self.milk > Requirement.milk)
        )

    def validate_money(self):
        return self.money > Requirement.money

    def insert_money(self, coin):
        if coin == "q":
            new_money = 0.25
        elif coin == "d":
            new_money = 0.10
        elif coin == "n":
            new_money = 0.05
        elif coin == "p":
            new_money = 0.01
        elif coin == "dollar":
            new_money = 1
        self.money += new_money


if __name__ == "__main__":
    machine = Machine()

    while machine.operating:
        action = machine.prompt()
        if action == "espresso" or action == "latte" or action == "cappuccino":
            if not machine.validate_resources():
                print("No resources")
                continue
            while not machine.validate_money():
                print("Not enough money. Insert more money: ")
                coin = input("dollar = $1,vq = $0.25, d = $0.10, n = $0.05, p = $0.01: ")
                machine.insert_money(coin)
            machine.make_coffee()
        elif action == "report":
            machine.print_report()
        elif action == "off":
            machine.turn_off()
            machine.operating = False
        else:
            print("Select a valid input")
