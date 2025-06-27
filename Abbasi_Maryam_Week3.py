# DSC 510
# Week 3
# Programming Assignment Week 3
# Author: Maryam Abbasi
# Date: 06/22/2025

# This program asks the user how many feet of fiber optic cable they want.
# It gives a discount based on the length and shows the total price.
# It also includes basic error handling for invalid input.

# Welcome message
print("Welcome to the Fiber Cable Cost Estimator!")

# Get company name from the user
company_name = input("Please enter your company name: ")

# Get cable length from user and attempt to convert it to a number
cable_length_str = input("Enter the number of feet of cable you need: ")

try:
    cable_length = float(cable_length_str)

    # Check if the entered cable length is a positive number
    if cable_length <= 0:
        print("Error: Cable length must be a positive number greater than 0.")
    else:
        # Determine the price per foot based on the cable length
        if cable_length > 250:
            price_per_foot = 0.70
        elif cable_length > 100:
            price_per_foot = 0.80
        elif cable_length >= 50:
            price_per_foot = 0.90
        else:
            price_per_foot = 0.95

        # Calculate the total cost
        total_cost = cable_length * price_per_foot

        # Print the formatted receipt
        print("\n---------- Installation Receipt ----------")
        print(f"Company Name:        {company_name}")
        print(f"Feet Requested:      {cable_length} ft")
        print(f"Price per Foot:      ${price_per_foot:.2f}") # Formatted to 2 decimal places
        print("------------------------------------------") # Adjusted for consistent length
        print(f"Total Installation:  ${total_cost:.2f}")   # Formatted to 2 decimal places
        print("==========================================") # Adjusted for consistent length

except ValueError:
    # Handle cases where the user input is not a valid number
    print("Error: Invalid input! Please enter a numerical value for the cable length.")