name="Harrison"
print(f"hello {name}, welcome to the system ")
# doing math
a=20
b=4
c=int(a/b)
print (c)
i=50
for i in range(5):
    print("hello") 
# Displaying a message
print("good work") 
todo_list = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for index, task in enumerate(todo_list, start=1):
            status = "✔" if task['done'] else "✘"
            print(f"{index}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({"title": title, "done": False})
    print("Task added.")

def mark_done():
    view_tasks()
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todo_list):
        todo_list[index]['done'] = True
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print(f"Deleted: {removed['title']}")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter choice: ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
