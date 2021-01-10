class Vehicle:
    
    def __init__(self, name, seating_capacity, max_speed):
        self.name = name 
        self.seating_capacity = seating_capacity
        self.max_speed = max_speed

    def seating_capact(self):
        return f"The seating capacity of the vehicle {self.name} is {self.seating_capacity} and max speed is {self.max_speed}"

p1 = Vehicle("Volvo", 24,240)
print(p1.seating_capact())