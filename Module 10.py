# Answer to the question No-01
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print(f"Elevator is currently at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print(f"Elevator is currently at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top or target_floor < self.bottom:
            print("Invalid floor.")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

# Main Program
h = Elevator(0, 10)
print("--- Elevator moving to floor 5 ---")
h.go_to_floor(5)
print("--- Elevator returning to bottom floor ---")
h.go_to_floor(0)
print()

# Answer to the question no-02
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        print(f"\nRunning Elevator {elevator_num} to floor {target_floor}")
        self.elevators[elevator_num].go_to_floor(target_floor)

# Main Program
my_building = Building(0, 12, 3)
my_building.run_elevator(0, 7)
my_building.run_elevator(1, 4)
print()

# Answer to the question no-03
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        self.elevators[elevator_num].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n!!! FIRE ALARM !!! Moving all elevators to bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i+1}:")
            elevator.go_to_floor(self.bottom)

# Main Program
city_hall = Building(0, 20, 2)
print(f"---Elevator-01---")
city_hall.run_elevator(0, 15)
print(f"---Elevator-02---")
city_hall.run_elevator(1, 8)
city_hall.fire_alarm()
print()

# Answer to the question no-04
import random
class Car:
    def __init__(self, registration, top_speed):
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.distance = 0

    def drive(self, hours=1):
        self.distance += self.speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.speed = max(0, min(car.top_speed, car.speed + change))
            car.drive()

    def print_status(self):
        print(f"\n--- {self.name} Status ---")
        print(f"{"Reg No":<10} | {"Top Speed":<8} | {"Cur Speed":<8} | {"Distance":<10}")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.registration:<10} | {car.top_speed:<8} | {car.speed:<8} | {car.distance:<10.1f}")

    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)

# Main Program
race_cars = [Car(f"CAR-{i + 1}", random.randint(100, 200)) for i in range(10)]
derby = Race("Grand Demolition Derby", 8000, race_cars)

hours_elapsed = 0
while not derby.race_finished():
    derby.hour_passes()
    hours_elapsed += 1

    if hours_elapsed % 10 == 0:
        print(f"\nStatus after {hours_elapsed} hours:")
        derby.print_status()

print(f"\nRace finished in {hours_elapsed} hours!")
derby.print_status()
print()