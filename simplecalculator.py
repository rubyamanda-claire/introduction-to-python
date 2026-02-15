# Simple Calculator with Loop

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y


while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator... Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))

            elif choice == '2':
                print("Result:", subtract(num1, num2))

            elif choice == '3':
                print("Result:", multiply(num1, num2))

            elif choice == '4':
                print("Result:", divide(num1, num2))

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    else:
        print("Invalid choice! Please select a valid option.")


# Added a while True: loop so the program keeps running.
# Added an Exit option (5).
# Used break to stop the loop.
# Added try-except to handle invalid number input.