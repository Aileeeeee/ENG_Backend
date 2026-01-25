"""Using the concept of classes and object to build a CLI task manger that has the following features:
● Add tasks with descriptions and due dates 
● Mark tasks as complete 
● View all tasks (pending and completed)
● Delete tasks ● Save tasks to a JSON file (persistence) 
● Load tasks when the program starts
"""
# Import JSON library
import json

# Define Task class
class Task:
    def __init__(self,task_description="",task_due_date="",task_status="Pending"):
        self.task_description = task_description
        self.task_due_date = task_due_date
        self.task_status = task_status
    
    def to_dict(self):
        # Storing task details in a dictionary to represent a specific task
        task_dict = {"task_description":self.task_description,
                     "task_due_date":self.task_due_date,
                     "task_status":self.task_status}
        
        return task_dict
    


class TaskManger:
    def __init__(self):
        self.tasks = {}
        self.filename = "tasks.json"

    def add_task(self):
        task_id = len(self.tasks) + 1
        task = Task(task_description,task_due_date)
        self.tasks[task_id] = task.to_dict()      
        return self.tasks
        
    
    def delete_task(self,task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        
            # Reordering dictionary key index
            all_tasks = list(self.tasks.values())
            self.tasks.clear()
            
            for index, task in enumerate(all_tasks, start = 1):
                self.tasks[index] = task

            return True
        else:
            return False
        
    def complete_task(self,task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["task_status"] = "Completed"
            return True
        else:
            return  False
        
    def save_to_json(self):
        with open(self.filename,"w") as file:
            json.dump(self.tasks,file,indent=4)

    def load_to_json(self):
        try:
            with open(self.filename,"r") as file:
                loaded_tasks = json.load(file)
                return {int(key): value for key,value in loaded_tasks.items()}
        except FileNotFoundError:
            return {}        

task_manager = TaskManger()   
task_manager.tasks = task_manager.load_to_json()

while True:

    print("\nCommand Line Task Manager Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task Complete")
    print("4. Display all tasks")
    print("5. Exit Task Manager")

    choice = input("Select an option: ")
    
    if choice == "1":
        # Get task details
        task_description = input("Enter task description (e.g Buy groceries): ").title()
        task_due_date = input("Enter task due date (DD-MM-YYYY): ")
        task_manager.add_task()
        task_manager.save_to_json()
        print("Task added.")

    elif choice == "2":
        for key , task in task_manager.tasks.items():
            print(f"{key}. {task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")

        choice = int(input("Select option: "))

        if task_manager.delete_task(choice):
            task_manager.save_to_json()
            print("Task deleted.")
        else:
            print("Invalid choice. Task not found in task manager!")

    elif choice == "3":
        for key , task in task_manager.tasks.items():
            print(f"{key}. {task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")


        choice = int(input("Pick a task to mark complete:"))        
        
        if task_manager.complete_task(choice):
            task_manager.save_to_json()
            print("Task marked completed")

    elif choice == "4":
        found = False

        # Print all pending tasks
        print("\nPending Tasks")
        for key, task in task_manager.tasks.items():
            if task["task_status"] == "Pending":
                print(f"{task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")
                found = True

        if not found:
            print("No pending tasks found.")

        found = False
        # Print all completed tasks
        print("\nCompleted Tasks")
        for key, task in enumerate(task_manager.tasks.values(), start=1):
            if task["task_status"] == "Completed":
                print(f"{task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")
                found = True

        if not found:
            print("No completed tasks found.")
    


    elif choice == "5":
        print("Exiting Command Line Task Manager..........")
        break

    else:
        print("Invalid choice!")

    
print(task_manager.tasks)


