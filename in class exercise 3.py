""" attributes assignment #3
course: COSC-1100
Malkom Mcfarlane
date:2026-09-29
Description:This program will ask name, excerise mark, hours studied per week and attendance mode  """

#OUTPUT 
#Display the name, excercise mark, hours studied per week and attendance mode

#INPUT
#Ask the user to enter their name that can't be blank or contain any spaces,input an excercise mark thats a whole number from 0 to 100
# , hours studied per week A number from 0 to 168; decimals are allowed. and attendance mode Must be “Online,” “In person,” or “Hybrid”

#PROCCESS
#first ask for name.If the name is blank or contains spaces, ask the user to enter their name again.
#Then ask for the excercise mark. If the mark is not a whole number from 0 to 100, ask the user to enter their mark again.
#Then ask for the hours studied per week. If the hours is not a number from 0 to 168, ask the user to enter their hours again.
#Then ask for the attendance mode. If the mode is not “Online,” “In person,” or “Hybrid,” ask the user to enter their mode again.

#PSEUDOCODE
#ask for user name, 
# if name is blank or contains spaces,do not validate 
# if name is corrct validate the name
# ask for excercise mark
# if mark is not a whole number from 0 to 100, ask user to enter mark again
# ask for hours studied per week
# if hours is not a number from 0 to 168, ask user to enter hours again
# ask for attendance mode
# if mode is not “Online,” “In person,” or “Hybrid,” ask user to enter mode again.

user_name = input("Enter your name (no spaces): ")

if user_name == "" or " " in user_name:
 print("Invalid name. Please enter a valid name without spaces.")



excercise_mark = input("Enter your exercise mark (whole number from 0 to 100): ")
if not excercise_mark.isdigit() or not (0 <= int(excercise_mark) <= 100):
 print("Invalid mark. Please enter a whole number between 0 and 100.")
 

hours_studied = input("Enter hours studied per week (0 to 168): ")
if not hours_studied.replace('.', '').isdigit() or not (0 <= float(hours_studied) <= 168):
 print("Invalid hours. Please enter a number between 0 and 168.")

attendance_mode = input("Enter attendance mode (Online, In person, or Hybrid): ")
if attendance_mode not in ["Online", "In person", "Hybrid"]:
 print("Invalid attendance mode. Please enter 'Online', 'In person', or 'Hybrid'.")

 