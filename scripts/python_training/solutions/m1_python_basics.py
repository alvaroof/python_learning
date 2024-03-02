# -*- coding: utf-8 -*-
"""Solutions for the tasks 1 and 2 of module 1: Python Basics."""
from loguru import logger

"""TASK 1"""


class Vehicle:
    """Class Vehicle."""

    def __init__(
        self,
        brand: str,
        color: str,
        max_capacity: int,
        speed: float,
        power_source: str,
        current_position: float,
    ) -> None:
        self.brand = brand
        self.color = color
        self.max_capacity = max_capacity
        self.speed = speed
        self.power_source = power_source
        self.current_position = current_position

    def accelerate(self, acc: float, time: int) -> None:
        """Calculate the new speed after accelerating.

        :param acc: Rate at which the vehicle is accelerating, in m/s**2.
        :param time: Time that the acceleration lasts, in seconds.
        """
        self.current_position = self.current_position + self.speed * time + 0.5 * acc * time**2
        self.speed = self.speed + acc * time
        logger.info(f"Accelerated to {self.speed} m/s.")

    def brake(self, dec: float, time: int) -> None:
        """Calculate the new speed after braking. The speed can not be less than 0.

        :param dec: Rate at which the vehicle is accelerating, in m/s**2.
        :param time: Time that the acceleration lasts, in seconds.
        """
        self.current_position = self.current_position + self.speed * time + 0.5 * dec * time**2
        self.speed = max(0, self.speed - dec * time)
        logger.info(f"Applied brakes. Current speed: {self.speed} m/s.")

    def repaint(self, new_color: str) -> None:
        """Change the color of the vehicle.

        :param new_color: New color of the vehicle.
        """
        self.color = new_color
        logger.info(f"{self.brand} has been repainted to {new_color}.")

    def maintain_speed(self, time: int) -> None:
        """Calculate the position after maintaining the same speed for n seconds.

        :param time: Time that the speed is maintained, in seconds.
        """
        self.current_position = self.current_position + self.speed * time
        logger.info(f"{self.brand} is maintaining speed of {self.speed} km/h for {time} hours.")


"""This is an example of how we could use the class
trambesos = Vehicle(brand = "Alstom", color = "Blue", max_capacity = 150,
speed = 0, power_source = "Electric", current_position = 0)

trambesos.accelerate(15, 4)
trambesos.maintain_speed(54)
trambesos.brake(30, 2)

distance_run = trambesos.current_position
"""


"""TASK 2"""


class Car(Vehicle):
    """Class Car inheriting from Vehicle."""

    def __init__(
        self,
        brand: str,
        color: str,
        max_capacity: int,
        speed: float,
        power_source: str,
        current_position: float,
        wheels: int,
        license_plate: str,
        max_fuel: float,
        fuel_left: float,
        max_trunk_space: float,
        trunk_space_left: float,
        consumption_per_km: float,
    ) -> None:
        super().__init__(brand, color, max_capacity, speed, power_source, current_position)
        self.wheels = wheels
        self.license_plate = license_plate
        self.max_fuel = max_fuel
        self.fuel_left = fuel_left
        self.max_trunk_space = max_trunk_space
        self.trunk_space_left = trunk_space_left
        self.consumption_per_km = consumption_per_km

    def register_license(self, new_license: str) -> None:
        """Change the current license to a new one.

        :param new_license: New license of the car.
        """
        self.license_plate = new_license
        logger.info(f"License plate registered: {new_license}")

    def refuel(self, liters: float) -> None:
        """Refill the amount of fuel left.

        :param liters: Liters of fuel added.
        """
        self.fuel_left = max(self.max_fuel, self.fuel_left + liters)
        logger.info(f"Refueled {liters} liters. Total fuel now: {self.fuel_left} liters.")

    def fill_trunk(self, volume: float) -> None:
        """Load objects into the trunk.

        :param volume: Volume of the objects added.
        """
        self.trunk_space_left = max(0, self.trunk_space_left - volume)
        logger.info(f"Filled trunk with {volume} m3. Space remaining: {self.trunk_space_left} m3.")

    def empty_trunk(self, volume: float) -> None:
        """Remove objects from the trunk.

        :param volume: Volume of the objects removed.
        """
        self.trunk_space_left = max(self.max_trunk_space, self.trunk_space_left + volume)
        logger.info(
            f"Emptied {volume} m3 from the trunk. Space remaining: {self.trunk_space_left} m3."
        )


"""This is an example of how we could use the class.
car_instance = Car(brand="Toyota", color="Blue", max_capacity=5, speed=60,
                  power_source="Gasoline", current_position=(0, 0),
                  wheels=4, license_plate="ABC123", fuel_left=20,
                  trunk_space_left=3, consumption_per_km=0.1)

car_instance.register_license("XYZ789")
car_instance.refuel(10)
car_instance.accelerate(10, 2)
car_instance.fill_trunk(2)
car_instance.empty_trunk(1)
"""


class Boat(Vehicle):
    """Class Boat inheriting from Vehicle."""

    def __init__(
        self,
        brand: str,
        color: str,
        max_capacity: int,
        speed: float,
        power_source: str,
        current_position: float,
        engines: int,
        food_supply_kg: float,
        passengers: int,
        destination: str,
        crew: list,
    ) -> None:
        super().__init__(brand, color, max_capacity, speed, power_source, current_position)
        self.engines = engines
        self.food_supply_kg = food_supply_kg
        self.passengers = passengers
        self.destination = destination
        self.crew = crew

    def board(self, num_passengers: int) -> None:
        """Increase the number of passengers.

        :param num_passengers: The amount of passengers that board.
        """
        self.passengers += num_passengers
        logger.info(f"Boarded {num_passengers} passengers. Total passengers now: {self.passengers}")

    def resupply(self, kg_food: float) -> None:
        """Resupply the food left on the boat.

        :param kg_food: Kilograms of food added to the supply.
        """
        self.food_supply_kg += kg_food
        logger.info(
            f"Resupplied {kg_food} kg of food. Total food supply now: {self.food_supply_kg} kg."
        )

    def dock(self) -> None:
        """Dock the boat."""
        logger.info("The boat has docked.")

    def update_destination(self, new_dest: str) -> None:
        """Update the destination of the boat after docking.

        :param new_dest: The new destination of the boat.
        """
        self.destination = new_dest
        logger.info(f"Destination updated to {new_dest}.")


"""This is an example of how we could use the class.
boat_instance = Boat(brand="SeaMaster", color="White", max_capacity=50, speed=30,
                    power_source="Diesel", current_position=(0, 0),
                    engines=2, food_supply_kg=100, passengers=10, destination="Island A",
                    crew=["Captain John", "Chief Engineer Sarah", "Deckhand Mike", "Mate Emily"])

boat_instance.board(5)
boat_instance.accelerate(15, 1)
boat_instance.resupply(50)
boat_instance.update_destination("Island B")
boat_instance.dock()
"""


class Bike(Vehicle):
    """Class Bike inheriting from Vehicle."""

    def __init__(
        self,
        brand: str,
        color: str,
        max_capacity: int,
        speed: float,
        power_source: str,
        current_position: float,
        wheels: int,
        owner: str,
        size: int,
        bike_type: str,
        gear_transmission: str,
    ) -> None:
        super().__init__(brand, color, max_capacity, speed, power_source, current_position)
        self.wheels = wheels
        self.owner = owner
        self.size = size
        self.bike_type = bike_type
        self.gear_transmission = gear_transmission

    def change_owner(self, new_owner: str) -> None:
        """Change the owner of the bike.

        :param new_owner: The new owner of the bike.
        """
        self.owner = new_owner
        logger.info(f"Changed owner to {new_owner}.")

    def change_transmission(self, new_trans: str) -> None:
        """Change the gear transmission of the bike.

        :param new_trans: The new transmission.
        """
        self.gear_transmission = new_trans
        logger.info(f"Changed transmission to {new_trans}.")


"""This is an example of how we could use the class.
bike_instance = Bike(brand="MountainBike", color="Red", max_capacity=1, speed=20,
                    power_source="Manual", current_position=(0, 0),
                    wheels=2, owner="Alice", size="Medium",
                    bike_type="Mountain", gear_transmission="7-speed")

bike_instance.accelerate(10, 2)
bike_instance.change_owner("Bob")
bike_instance.change_transmission("5-speed")
"""
