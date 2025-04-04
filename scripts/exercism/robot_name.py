import random
import string

class Robot:
    robot_names = []
    def __init__(self):
        self.name = self.assign_random_name()
        self.robot_names.append(self.name)

    def reset(self):
        self.name = self.assign_random_name()
        
    def generate_random_name(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        digits = ''.join(random.choices(string.digits, k=3))
        return letters + digits

    def assign_random_name(self):
        candidate_name = self.generate_random_name()
        while candidate_name in Robot.robot_names:
            candidate_name = self.generate_random_name()
        return candidate_name
