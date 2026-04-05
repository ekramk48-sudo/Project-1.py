# Answer to the question no-01
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}, Pages: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

if __name__ == "__main__":
    mag = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)

    mag.print_information()
    print("-" * 25)
    book.print_information()
    print("-" * 32)


# Answer to the question no-02
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.current_speed = 100
gasoline_car.current_speed = 120

electric_car.drive(3)
gasoline_car.drive(3)

print(f"---Distance travelled details of 2 car---")
print(f"Electric Car Distance travelled: {electric_car.distance_traveled} km")
print(f"Gasoline Car Distance travelled: {gasoline_car.distance_traveled} km")