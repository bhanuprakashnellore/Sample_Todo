"""name="Bhanuprakash"
age=20
print(f"Name: {name}")
print(f"Age: {age}")"""


#name = input("Please enter your name : ")
#print("Hello "+name+" welcome to python learning")

"""number=int(input("Enter the number:"))
if (number %2==0):
  print("It is a Even Number")
else:
    print("Not an Even Number")
    
    
age=int(input("Enter your age:"))
if age>=18:
    print("Your are eligible to vote")
else:
    print("Your are not eligible to vote")"""
    
     
"""marks=int(input("Enter the Marks:"))
if(marks>=90):
    print("Grade A")
elif(marks>=80):
    print("Grade B")
elif(marks>=70):
    print("Grade C")
elif(marks>=60):
    print("Grade D")
else:
    print("Grade F")
    
    
for i in range(10):
    print(f"count :{i}")"""
    
"""states=["Andhra","Goa","Kerala","Telangana"]
for state in states:
    print(state)
    
 """
 
 
 # Simple CLI To-Do Manager with Category

# To-Do Manager using Class

class TodoManager:

    def __init__(self):
        self.tasks = []

    # -------------------------
    # Add Task
    # -------------------------
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

    # -------------------------
    # View Tasks
    # -------------------------
    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.\n")
            return

        for i in range(len(self.tasks)):
            status = "Completed" if self.tasks[i]["completed"] else "Not Completed✘"

            print(f"{i + 1}. {self.tasks[i]['task']}")
            print(f"   Category: {self.tasks[i]['category']}")
            print(f"   Status: {status}\n")

    # -------------------------
    # Complete Task
    # -------------------------
    def complete_task(self):
        self.view_tasks()
        num = int(input("Enter task number to complete: ")) - 1

        if 0 <= num < len(self.tasks):
            self.tasks[num]["completed"] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")

    # -------------------------
    # Delete Task
    # -------------------------
    def delete_task(self):
        self.view_tasks()
        num = int(input("Enter task number to delete: ")) - 1

        if 0 <= num < len(self.tasks):
            self.tasks.pop(num)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number!\n")


# -------------------------
# Main Program
# -------------------------

todo = TodoManager()

while True:
    print("===== OOP TO-DO MANAGER =====")
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
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice!\n")