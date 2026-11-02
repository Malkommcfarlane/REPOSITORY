


print("\nSquare  number finder")

for i in range(1, 30):
    print("*", end='')

while True:
  try:
   lower_bound = int(input("\nEnter a lower bound (1-10000): "))
   Iresult=math.sqrt(lower_bound)
   break 
 
  except ValueError:
   if lower_bound < 1 or lower_bound > 1000:
        print("Invalid input. Please enter a whole number between 1 and 10000.")
        if lower_bound is float():
            print("Invalid input. Please enter a whole number between 1 and 10000.")
if lower_bound is str():
        print("Invalid input. Please enter a whole number between 1 and 10000.")



