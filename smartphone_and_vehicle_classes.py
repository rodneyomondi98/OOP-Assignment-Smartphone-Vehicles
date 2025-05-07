# Base class for a generic smartphone
class Smartphone:
    # Initialize smartphone with brand, model, storage, and battery attributes
    def __init__(self, brand, model, storage, battery):
        self.brand = brand        # Brand of the smartphone (e.g., Samsung)
        self.model = model        # Model name (e.g., Galaxy A54)
        self.storage = storage    # Storage capacity (e.g., 128GB)
        self.battery = battery    # Battery percentage (e.g., 80)

    # Method to simulate making a phone call
    def make_call(self, number):
        print(f"{self.model} is calling {number}...")

    # Method to simulate charging the phone and display battery level
    def charge(self):
        print(f"{self.model} is charging... Battery at {self.battery}%")

# Subclass that inherits from Smartphone, specialized for gaming
class GamingSmartphone(Smartphone):
    # Initialize gaming smartphone with additional refresh_rate attribute
    def __init__(self, brand, model, storage, battery, refresh_rate):
        # Call the parent class's __init__ to set inherited attributes
        super().__init__(brand, model, storage, battery)
        self.refresh_rate = refresh_rate  # Screen refresh rate (e.g., 144Hz)

    # Method to simulate playing a game with refresh rate details
    def play_game(self, game):
        print(f"Playing {game} at {self.refresh_rate}Hz on {self.model}!")

# Testing the classes with example instances
# Create a generic smartphone instance
phone1 = Smartphone("Samsung", "Galaxy A54", "128GB", 80)
phone1.make_call("0712345678")  # Test the make_call method
phone1.charge()                 # Test the charge method

# Create a gaming smartphone instance
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", "256GB", 90, 144)
gaming_phone.make_call("0799999999")  # Test inherited make_call method
gaming_phone.play_game("Asphalt 9")   # Test play_game method


# Base class defining a generic vehicle
class Vehicle:
    # Abstract method to be overridden by subclasses
    def move(self):
        # Raise an error if this method is not overridden in a subclass
        raise NotImplementedError("This method should be overridden.")

# Subclass representing a car, inheriting from Vehicle
class Car(Vehicle):
    # Override the move method to define car-specific behavior
    def move(self):
        print("Driving 🚗")  # Prints car movement with emoji

# Subclass representing a plane, inheriting from Vehicle
class Plane(Vehicle):
    # Override the move method to define plane-specific behavior
    def move(self):
        print("Flying ✈️")  # Prints plane movement with emoji

# Subclass representing a boat, inheriting from Vehicle
class Boat(Vehicle):
    # Override the move method to define boat-specific behavior
    def move(self):
        print("Sailing 🚢")  # Prints boat movement with emoji

# Test polymorphism by creating a list of different vehicle instances
vehicles = [Car(), Plane(), Boat()]

# Iterate through the list and call move() on each vehicle
for vehicle in vehicles:
    vehicle.move()  # Demonstrates polymorphic behavior