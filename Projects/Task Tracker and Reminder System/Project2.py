#Task Tracker and Reminder System

def add_task(task_list):
    task = input("\nEnter the task: ").strip()
    task_list.append({"task": task, "Status of Task": "Pending"})
    print(f"Task '{task}' added successfully.")
    print("\n")

def view_tasks(task_list):
    if not task_list:
        print("No tasks found.\n")
    else:
        print("\nTasks:")
        for i in range(len(task_list)):
            task = task_list[i]
            print(f"{i + 1}. {task['task']} - {task['Status of Task']}")
        print("\n")    

def mark_as_completed(task_list):
    view_tasks(task_list)
    if task_list:
        try :
            task_index = int(input("\nEnter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(task_list):
                task_list[task_index]["Status of Task"] = "Completed"
                print("Task marked as completed.\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid task number.\n")

def delete_task(task_list):
    view_tasks(task_list)
    if task_list:
        try :
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(task_list):
                deleted_task = task_list.pop(task_index)
                print(f"Task '{deleted_task['task']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def mainMenu():
    print("Welcome to Task Tracker and Reminder System".center(80, "-"))
    print("Task Tracker Menu:")

    task_list = []
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                add_task(task_list)
            case "2":
                view_tasks(task_list)
            case "3":
                mark_as_completed(task_list)
            case "4":
                delete_task(task_list)
            case "5":
                if choice == "5":
                    print("Goodbye! Have a nice day.")
                    break           
            case _:
                print("Invalid choice. Please try again.")

mainMenu()