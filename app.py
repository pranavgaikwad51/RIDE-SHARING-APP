# Project 2: Ride Sharing App

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Driver(User):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
        self.available = True

    def __str__(self):
        return f"Driver: {self.name}, Vehicle: {self.vehicle}"

class Passenger(User):
    def request_ride(self, app):
        driver = app.assign_driver()
        if driver:
            print(f"{self.name} is riding with {driver.name} in {driver.vehicle}")
            driver.available = False
        else:
            print("No drivers available.")

class RideShareApp:
    def __init__(self):
        self.drivers = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def assign_driver(self):
        for driver in self.drivers:
            if driver.available:
                return driver
        return None

# Example usage
if __name__ == "__main__":
    app = RideShareApp()
    app.add_driver(Driver("Ravi", "Honda City"))
    app.add_driver(Driver("Sita", "Hyundai Creta"))

    p1 = Passenger("Arjun")
    p2 = Passenger("Meera")

    p1.request_ride(app)
    p2.request_ride(app)
    p2.request_ride(app)  # Should say no drivers available
