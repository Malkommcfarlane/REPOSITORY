""" assignmernt 1 iteration
course: COSC-1100
Malkom Mcfarlane
date:2026-11-01
Description: this program will ask the user to enter a lower bound and upper bound that have to be whole numbers."""
#Input
#Ask the user to enter a lower bound and upper bound that are whole numbers from 1 to 10000

#Output
#Display the lower bound and upper bound

#proccess
#Ask the user to enter a lower bound and upper bound that are whole numbers from 1 to 10000. If the lower bound or upper bound is not a whole number from 1 to 10000, ask the user to enter their lower bound and upper bound again.

#Pseudocode
#Ask the user to enter a lower bound and upper bound that are whole numbers from 1 to 10000
#If the lower bound or upper bound is not a whole number from 1 to 10000, ask the user to enter their lower bound and upper bound again.    

print("\nSQUARE NUMBER FINDER")



lower_bound = input(" Lower bound enter a number between 1 and 10000: ")
if lower_bound.isdigit() and (1 <= int(lower_bound) <= 10000):
    print("Correct input.")
if not lower_bound.isdigit() or not (1 <= int(lower_bound) <= 10000):
    print("Invalid input. Please enter a whole number between 1 and 10000.")
    lower_bound = input("Enter a number between 1 and 10000: ")
    while not lower_bound.isdigit() or not (1 <= int(lower_bound) <= 10000):
        print("Invalid input. Please enter a whole number between 1 and 10000.")
        lower_bound = input("Enter a number between 1 and 10000: ")
    else:

      print("Correct input.")






upper_bound = input(" Upper bound enter a number between 1 and 10000: ")
if upper_bound.isdigit() and (1 <= int(upper_bound) <= 1000):
    print("Correct input.")
if not upper_bound.isdigit() or not (1 <= int(upper_bound) <= 10000):
    print("Invalid input. Please enter a whole number between 1 and 10000.")
    upper_bound = input("Enter a number between 1 and 10000: ")
    while not upper_bound.isdigit() or not (1 <= int(upper_bound) <= 10000):
        print("Invalid input. Please enter a whole number between 1 and 1000.")
        upper_bound = input("Enter a number between 1 and 1000: ")
    else:

      print("Correct input.")




