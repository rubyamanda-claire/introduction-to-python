while True:
    print("\nArea of a Trapezium Calculator")
    print("1. Calculate Area")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == '2':
        print("Exiting program... Goodbye!")
        break

    if choice == '1':
        try:
            a = float(input("Enter the length of first parallel side (a): "))
            b = float(input("Enter the length of second parallel side (b): "))
            h = float(input("Enter the height (h): "))

            area = 0.5 * (a + b) * h

            print("The Area of the Trapezium is:", area)

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    else:
        print("Invalid choice! Please select 1 or 2.")