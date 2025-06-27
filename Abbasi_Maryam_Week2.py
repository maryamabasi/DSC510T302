# DSC 510
# Week 2
# Programming Assignment Week 2
# Author: Maryam Abbasi
# 06/15/2025

# Change Control Log:
# Change#: 1
# Change(s) Made: Initial version of the program created.
# Date of Change: 06/15/2025
# Author: Maryam Abbasi
# Change Approved by: Maryam Abbasi
# Date Moved to Production: 06/15/2025
# -----------------------------------------------------
# ------------------------------------------------------
# This program calculates the cost of fiber optic cable installation
# based on the number of feet entered by the user. It multiplies
# the number of feet by $0.95 per foot and prints a receipt.
# ------------------------------------------------------
# ------------------------------------------------------


# Display a welcome message to the user
print("Welcome to the Fiber Optic Cable Installation Cost Calculator!")

# Get company name from user
company_name = input("Please enter your company name: ")

#  Get the number of feet of cable required from the user
feet_requested = input("Enter the number of feet of fiber optic cable to be installed: ")

# Convert input to float
feet_requested = float(feet_requested)

# Calculate the cost at $0.95 per foot
cost_per_foot = 0.95
total_cost = feet_requested * cost_per_foot

# Print a receipt including company name, feet of cable, and total cost
print("\n---------- Installation Receipt ----------")
print(f"Company Name:           {company_name}")
print("_________________________________________________")
print(f"Feet Requested:          {feet_requested} ft")
print("_________________________________________________")
print(f"Cost per Foot:           ${cost_per_foot}")
print("_________________________________________________")
print(f"Total Installation Cost: ${total_cost:.2f}")
print("_________________________________________________")
