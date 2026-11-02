


task = input("Enter a task (or 'q' to quit): ")
while task != "q":
    print(f"Task '{task}' has been processed.")
    task = input("Enter next task: ")

count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  
