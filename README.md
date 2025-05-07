# OOP-Assignment-Smartphone-Vehicles

This repository contains Python code examples demonstrating key Object-Oriented Programming (OOP) concepts, specifically **inheritance** and **polymorphism**. The examples are designed to be simple, educational, and easy to understand for learners and developers exploring OOP principles in Python.

## Table of Contents
- [Project Overview](#project-overview)
- [Code Examples](#code-examples)
  - [Example 1: Smartphone Inheritance](#example-1-smartphone-inheritance)
  - [Example 2: Vehicle Polymorphism](#example-2-vehicle-polymorphism)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Expected Output](#expected-output)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This repository serves as a learning resource for understanding two fundamental OOP concepts in Python:
- **Inheritance**: Creating a hierarchy of classes where a subclass inherits attributes and methods from a parent class.
- **Polymorphism**: Allowing different classes to be treated as instances of a common parent class, with each class implementing shared methods in its own way.

The code is commented for clarity and includes two distinct examples:
1. A **Smartphone** class hierarchy demonstrating inheritance.
2. A **Vehicle** class hierarchy showcasing polymorphism.

Each example is self-contained and can be run independently to observe the behavior of the OOP principles in action.

## Code Examples

### Example 1: Smartphone Inheritance
File: `smartphone.py`

This example demonstrates **inheritance** by creating a base `Smartphone` class and a derived `GamingSmartphone` class.

- **Base Class**: `Smartphone`
  - Attributes: `brand`, `model`, `storage`, `battery`
  - Methods:
    - `make_call(number)`: Simulates making a phone call.
    - `charge()`: Displays the charging status and battery percentage.
- **Subclass**: `GamingSmartphone`
  - Inherits from `Smartphone`.
  - Additional Attribute: `refresh_rate` (screen refresh rate).
  - Additional Method: `play_game(game)`: Simulates playing a game at the specified refresh rate.

**Key Features**:
- Uses `super().__init__()` to initialize parent class attributes.
- Extends functionality in the subclass while reusing base class methods.
- Includes comments for clarity.

**Code Snippet**:
```python
# Base class for a generic smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"{self.model} is calling {number}...")

    def charge(self):
        print(f"{self.model} is charging... Battery at {self.battery}%")

# Subclass that inherits from Smartphone, specialized for gaming
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, refresh_rate):
        super().__init__(brand, model, storage, battery)
        self.refresh_rate = refresh_rate

    def play_game(self, game):
        print(f"Playing {game} at {self.refresh_rate}Hz on {self.model}!")

# Testing
phone1 = Smartphone("Samsung", "Galaxy A54", "128GB", 80)
phone1.make_call("0712345678")
phone1.charge()

gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", "256GB", 90, 144)
gaming_phone.make_call("0799999999")
gaming_phone.play_game("Asphalt 9")