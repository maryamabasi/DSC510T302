# DSC 510
# Week 5
# Programming Assignment Week 5
# Author: Maryam Abbasi
# Date: 07/05/2025

# Description:
# This program allows the user to perform mathematical operations or calculate an average.
# It uses loops, functions, and error handling to demonstrate core Python programming concepts.

def perform_calculation(operation):
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2

        else:
            return "Invalid operation."

    except ValueError:
        return "Error: Please enter valid numbers."


def calculate_average():
    try:

        count = int(input("How many numbers do you want to average? "))
        if count <= 0:
            return "Error: Number must be greater than 0."

        total = 0
        for i in range(count):
            while True:
                try:
                    num = float(input(f"Enter number: {i + 1}: "))
                    total += num
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        average = total / count
        return f"The average of the {count} numbers is {average:.2f}"

    except ValueError:
        return "Error: Please enter a valid integer."


def main():
    print("Welcome to the Python Calculator and Averager!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Perform a calculation (+, -, *, /)")
        print("2. Calculate an average")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            op = input("Enter the operation ( + , - , *  or /): ")
            result = perform_calculation(op)
            print(f"Calculation result: {result} ")

        elif choice == "2":
            result = calculate_average()
            print(f"Average result: {result}")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Program starts here
if __name__ == "__main__":
    main()
