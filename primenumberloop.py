while True:
    print("\nPrime Number Checker")
    print("1. Check a Number")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == '2':
        print("Exiting program... Goodbye!")
        break

    if choice == '1':
        try:
            num = int(input("Enter a number: "))

            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        print(num, "is not a prime number.")
                        break
                else:
                    print(num, "is a prime number.")
            else:
                print(num, "is not a prime number.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    else:
        print("Invalid choice! Please select 1 or 2.")