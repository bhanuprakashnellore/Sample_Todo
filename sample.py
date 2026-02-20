
class TodoManager:


    def __init__(self):
        self.tasks = []

   
    def add_task(self):
        task_name = input("Enter task: ")
        category = input("Enter category: ")

        task = {
            "task": task_name,
            "category": category,
            "completed": False
        }

        self.tasks.append(task)
        print("Task added successfully!\n")

    
    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.\n")
            return

        for i in range(len(self.tasks)):
            status = "Completed" if self.tasks[i]["completed"] else "Not Completed"

            print(f"{i + 1}. {self.tasks[i]['task']}")
            print(f"   Category: {self.tasks[i]['category']}")
            print(f"   Status: {status}\n")

    
    def complete_task(self):
        self.view_tasks()
        num = int(input("Enter task number to complete: ")) - 1

        if 0 <= num < len(self.tasks):
            self.tasks[num]["completed"] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")


    def delete_task(self):
        self.view_tasks()
        num = int(input("Enter task number to delete: ")) - 1

        if 0 <= num < len(self.tasks):
            self.tasks.pop(num)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number!\n")




todo = TodoManager()

while True:
    print("===== TO-DO MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        todo.add_task()
    elif choice == "2":
        todo.view_tasks()
    elif choice == "3":
        todo.complete_task()
    elif choice == "4":
        todo.delete_task()
    elif choice == "5":
        print("Goodbye ")
        break
    else:
        print("Invalid choice!\n")