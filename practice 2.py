
#input validation for name, age, and children's names
#output
#display the name, age, and children's names
#process
#ask for dad's name. If the name is blank or contains spaces, ask the user to enter their name again.
#Then ask for mom's age. If the age is not a whole number from 0 to 100, ask the user to enter their age again.
#Then ask for the name of children. If the name is not "john", "paul", "george", or "ringo", ask the user to enter their name again.
#Pseudocode
#ask for dad's name
#if name is blank or contains spaces, do not validate
#ask for mom's age
#if age is not a whole number from 0 to 100, do not validate
#ask for name of children
#if name is not "john", "paul", "george", or "ringo", do not validate


dad = input("enter your name(no spaces):")

if dad == "" or " " in dad:
    print("Invalid name. Please enter a valid name without spaces.")

mom_age= input("enter mom age (whole number from 0 to 100):")
if not mom_age.isdigit() or not (0 <= int(mom_age) <= 100):
    print("Invalid age. Please enter a whole number between 0 and 100.")

Name_Of_Children = input("enter name of children (john, paul, george, ringo): ")
if Name_Of_Children not in ["john", "paul", "george", "ringo"]:
    print("Invalid name. Please enter 'john', 'paul', 'george', or 'ringo'.")
 