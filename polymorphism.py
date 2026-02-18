#An object-oriented programming concept that allows objects of different classes to be treated through a single, common interface, even if the underlying implementation of that interface is different for each class.

class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("The cat meows")

# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

# Polymorphism in action
animal.sound()
dog.sound()
cat.sound()

#All classes have a method called sound().
#Each class defines it differently.
#When we call sound(), Python decides which version to run based on the object.
#This is called polymorphism (same method name, different behavior).



     #POLYMORPHISM USING A LOOP
class Bird:
    def move(self):
        print("The bird flies")

class Fish:
    def move(self):
        print("The fish swims")

class Snake:
    def move(self):
        print("The snake slithers")

animals = [Bird(), Fish(), Snake()]

for animal in animals:
    animal.move()