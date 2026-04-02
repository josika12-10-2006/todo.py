tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == '2':
        show_tasks()

    elif choice == '3':
        show_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number")
        except:
            print("Error")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
