
# INHERITANCE (Method overriding is included)

class Animal:
    breath = "it does breath."

    def __init__(self):
        self.life = "yes"
        self.breath = "it does not breathe."

    def has_organs(self):
        l = "Any animal have the stomach."
        return l

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.n = name
        self.a = age

    def bark(self):
        p = f"Dog {self.n} of age {self.a} is barking. It also {self.life} and {self.has_organs()} Also, {Animal.breath} and no {self.breath}"
        print(p)

    def walk(self):
        print("Dog {self.n} of age {self.a} is walking.")
        

# METHOD OVERLOADING
        
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Usage
calc = Calculator()
result1 = calc.add(2, 3)        # Calls the first add method
result2 = calc.add(2, 3, 5)     # Calls the second add method


# Encapsulation - Getter & Setter methods
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)

# Trying to access private attribute directly (not allowed)
# print(account.__balance)  # This will raise an AttributeError



# COMPOSITION

# Component Class
class Engine:
    def __init__(self, engine_type, displacement):
        self.engine_type = engine_type
        self.displacement = displacement

    def start(self):
        print(f"Starting {self.engine_type} engine with {self.displacement} displacement.")

# Component Class
class Wheel:
    def __init__(self, size, material):
        self.size = size
        self.material = material

    def rotate(self):
        print(f"Rotating {self.material} wheel of size {self.size}.")

# Composite Class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine("V8", 5.7)  # Composition with Engine class
        self.wheels = [Wheel(18, "alloy"), Wheel(18, "alloy"), Wheel(18, "alloy"), Wheel(18, "alloy")]  # Composition with Wheel class

    def start(self):
        self.engine.start()
        print("Starting car...")

    def drive(self):
        for wheel in self.wheels:
            wheel.rotate()
        print(f"Driving {self.make} {self.model}...")

# Creating an instance of the Car class
car = Car("Toyota", "Camry")
car.start()
car.drive()



#ABSTRACTION
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()