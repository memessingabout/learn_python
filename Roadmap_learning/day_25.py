""" Day 25: Inheritance and Polymorphism """

class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Bark")
d = Dog()
d.speak()
