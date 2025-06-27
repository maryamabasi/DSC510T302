# DSC 510
# Week 4
# Programming Assignment Week 4
# Author: Maryam Abbasi
# Date: 06/29/2025

# This program calculates the total cost of fiber optic cable installation.
# It uses a separate function to calculate the cost and includes a main() function to run the program.
# The price per foot is based on the total feet requested.

# Function to calculate total cost
def calculate_total_cost(feet, price_per_foot):
    return feet * price_per_foot


# Main function
def main():
    print("Welcome to the Fiber Cable Cost Estimator!")

    # Get the company name
    company_name = input("Please enter your company name: ")

    # Ask user to enter the number of feet
    cable_length_str = input("Enter the number of feet of cable you need: ")

    try:
        cable_length = float(cable_length_str)

        if cable_length <= 0:
            print("Error: Please enter a number greater than 0.")
        else:
            # Determine the price per foot based on length
            if cable_length > 250:
                price_per_foot = 0.70
            elif cable_length > 100:
                price_per_foot = 0.80
            elif cable_length >= 50:
                price_per_foot = 0.90
            else:
                price_per_foot = 0.95

            # Calculate total cost using the function
            total_cost = calculate_total_cost(cable_length, price_per_foot)

            # Print receipt
            print("\n---------- Installation Receipt ----------")
            print(f"Company Name:        {company_name}")
            print(f"Feet Requested:      {cable_length} ft")
            print(f"Price per Foot:      ${price_per_foot:.2f}")
            print("------------------------------------------")
            print(f"Total Installation:  ${total_cost:.2f}")
            print("==========================================")

    except ValueError:
        print("Error: Please enter a valid numeric value for the cable length.")


# Call the main function to run the program
if __name__ == '__main__':
    main()
