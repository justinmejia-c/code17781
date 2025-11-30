def calculator():
    print("Simple Python Calculator")
    print("-------------------------")
    
    # Get numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter operation number (1-4): ")

    if choice == "1":
        result = num1 + num2
        op = "+"
    elif choice == "2":
        result = num1 - num2
        op = "-"
    elif choice == "3":
        result = num1 * num2
        op = "*"
    elif choice == "4":
        if num2 == 0:
            return print("Error: Cannot divide by zero!")
        result = num1 / num2
        op = "/"
    else:
        return print("Invalid choice. Please select 1–4.")

    print(f"\nResult: {num1} {op} {num2} = {result}")


# Run the calculator
calculator()
