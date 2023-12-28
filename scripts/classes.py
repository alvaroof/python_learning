# -*- coding: utf-8 -*-
from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class Bike:
    def __init__(
        self,
        description: str = "Really Beautiful",
        condition: str = "Perfect Condition",
        sale_price: float = 0,
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
        self.sale_price = sale_price
        self.cost = cost

        self.age = 2023 - year
        self.sold = False
        self.premium = None

    def update_sale_price(self, sale_price: float):
        if self.sold:
            raise AttributeError("Cannot update sale price of a sold bike.")
        if sale_price <= 0:
            raise ValueError("Sale price must be greater than zero.")
        self.sale_price = sale_price

    def is_premium(self):
        self.premium = "Yes"

    def sell(self) -> float:
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

    @staticmethod
    def sing_the_bike_song():
        print("Singing the Bike Song")


if __name__ == "__main__":
    my_bike = Bike(
        description="Black and Beautiful",
        condition=Condition.BAD,
        sale_price=1000,
        cost=100,
        year=1965,
    )
    print(my_bike)
    print(type(my_bike))
    print(my_bike.condition)
    my_bike.service(cost=100, new_condition=Condition.OKAY, new_sale_price=1200)
    print(my_bike.condition)
    my_bike.sell()
    my_bike.sing_the_bike_song()
