# -*- coding: utf-8 -*-
import random
import time
from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNowAllowed(Exception):
    pass


class Bike:
    num_wheels = 2
    counter = 0

    def __init__(
        self,
        description: str,
        condition: Condition = Condition.GOOD,
        sale_price: float = 100,
        cost: float = 0,
        year: int = 2015,
    ):
        """_summary_

        :param description: _description_, defaults to "Really Beautiful"
        :type description: str, optional
        :param condition: _description_, defaults to "Perfect Condition"
        :type condition: str, optional
        :param sale_price: _description_, defaults to 0
        :type sale_price: float, optional
        :param cost: _description_, defaults to 0
        :type cost: float, optional
        :param year: _description_, defaults to 2015
        :type year: int, optional
        """
        self.description = description
        self.condition = condition
        self._sale_price = None  # Private
        self.cost = cost
        self._slow_attribute = None

        self.age = 2023 - year
        self.sold = False
        self.premium = None
        self.update_sale_price(sale_price)
        Bike.counter += 1

    def update_sale_price(self, sale_price: float):
        if self.sold:
            raise MethodNowAllowed("Cannot update sale price of a sold bike.")
        if sale_price <= 0:
            raise ValueError("Sale price must be greater than zero.")
        self._sale_price = sale_price

    def is_premium(self):
        self.premium = "Yes"

    def sell(self) -> float:
        if self.sold:
            raise MethodNowAllowed("Cannot update sale price of a sold bike.")
        self.sold = True
        profit = self.sale_price - self.cost
        print(f"Sold for a profit: {profit}")
        return profit

    def service(self, cost, new_sale_price=None, new_condition=None):
        self.cost += cost
        if new_sale_price is not None:
            self.update_sale_price(new_sale_price)
        if new_condition is not None:
            self.condition = new_condition

    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price: float):
        if self.sold:
            raise MethodNowAllowed("Cannot update sale price of a sold bike.")
        if sale_price <= 0:
            raise ValueError("Sale price must be greater than zero.")
        self._sale_price = sale_price

    @property
    def profit(self):
        return self.sale_price - self.cost

    @property  # Used when an attribute is computationally intensive to calculate. Cache version is accessible
    def slow_attribute(self):
        if self._slow_attribute is not None:
            print("Slow Attribute was already cached")
            return self._slow_attribute
        else:
            print("Calculating Slow Attribute")
            time.sleep(5)
            self._slow_attribute = "Set"
            return self._slow_attribute

    @staticmethod
    def sing_the_bike_song():
        print("Singing the Bike Song")

    def __add__(self, other):
        if isinstance(other, Bike):
            self.cost += other.cost

    def __del__(self):
        Bike.counter -= 1
        print("Bike deleted")

    def __str__(self):
        """Called when str() or print()"""
        return f"{self.description}: ${self.sale_price}"

    def __repr__(self):
        return f"Bike({self.description}, {self.condition}, {self.sale_price}, {self.cost})"

    @staticmethod
    def get_test_bike():
        return Bike(condition=Condition.GOOD, sale_price=1000, cost=0, description=Bike.__name__)

    @classmethod
    def get_test_object(cls):
        return cls(
            condition=random.choice(list(Condition)),
            sale_price=1000,
            cost=0,
            description=f"{cls.__name__}",
        )


class Unicycle(Bike):
    num_wheels = 1


if __name__ == "__main__":
    my_bike = Bike(
        description="Black and Beautiful",
        condition=Condition.BAD,
        sale_price=1000,
        cost=100,
        year=1965,
    )
    test_unicycle = Unicycle.get_test_object()
    test_bike = Bike.get_test_bike()
    print(test_unicycle)
    print(test_bike)
    print([test_unicycle, test_bike])
    print(my_bike.slow_attribute)
    print(my_bike.slow_attribute)
