class Dog:

    def __init__(self,breed,age,colour):
        self.breed = breed
        self.age = age
        self.colour = colour

    def speak(self):
        print("Dog is barking")


dog1 = Dog("German Shepherd",5,"brown and black")
print(dog1.breed,dog1.age,dog1.colour)
dog1.speak()

dog2 =Dog("Samoyed", 3, "white")
print(dog2.breed,dog2.age,dog2.colour)
dog2.speak()

dog3 = Dog("Rottweiler", 7, "brown")
print(dog3.breed,dog3.age,dog3.colour)
