class Dog:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def bark(self):
        p = f"Dog {self.n} of age {self.a} is barking."
        print(p)

    def walk(self):
        print("Dog {self.n} of age {self.a} is walking.")
        

k = Dog("Tommy", 5)
k.bark()
k.a = 7
k.bark()