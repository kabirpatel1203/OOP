
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



