
age = 18 #Integer
temperature = 34.89 #Float
greeting = "Hey There" #String
isMarried = True #Boolean

print("I am",age,"years old")
print("The current body temperature of the patient is",temperature,"degrees celsius")
print(greeting,"Ruby")
print("Are you married?",isMarried)

#Data Structures - Multiple values stored in a single variable
cars = ["Audi","BMW","Toyota","Mercedes"] #List - Ordered and Changeable
languages = ["Python","Java", "C++"] #Array - Similar Datatypes
fruits = ("Banana", "Mango", "Grapes", "Pineapple") #Tuple - Ordered and Unchangeable
countries = {"Italy", "Germany","France", "Spain"} #Set - Unordered and Unchangeable
student = {
    "firstname" : "Ruby Mwago",
    "age" : 18,
    "course" : "FullStack",
    "gender" : "Male",
}  #Dictionary

print(cars)
print(fruits)
print(countries)
print(student)
print(student["firstname"])

#Typecasting - Converting one datatype to another

print(int(temperature))