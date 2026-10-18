tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                if tasks[i]["completed"]:
                    print(i + 1, ".", tasks[i]["task"], "- Completed")
                else:
                    print(i + 1, ".", tasks[i]["task"], "- Pending")

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            number = int(input("Enter task number to complete: "))

            if number >= 1 and number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task completed!")
            else:
                print("Invalid task number.")

    elif choice == 4:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            number = int(input("Enter task number to delete: "))

            if number >= 1 and number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted!")
            else:
                print("Invalid task number.")

    elif choice == 5:
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice!")