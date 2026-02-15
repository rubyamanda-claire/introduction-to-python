
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first > second and first > third:
    print(first,"is the largest number")

elif second > first and second > third:
    print(second,"is the largest number")

else:
    print(third,"is the largest number")