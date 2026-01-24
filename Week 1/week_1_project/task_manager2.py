"""Using the concept of classes and object to build a CLI task manger that has the following features:
● Add tasks with descriptions and due dates 
● Mark tasks as complete 
● View all tasks (pending and completed)
● Delete tasks ● Save tasks to a JSON file (persistence) 
● Load tasks when the program starts
"""

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
        
    
        
            

task_manager = TaskManger()   

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
        print("Task added.")

    elif choice == "2":
        for key , task in task_manager.tasks.items():
            print(f"{key}. {task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")

        choice = int(input("Select option: "))

        if task_manager.delete_task(choice):
            print("Task deleted.")
        else:
            print("Invalid choice. Task not found in task manager!")

    elif choice == "3":
        for key , task in task_manager.tasks.items():
            print(f"{key}. {task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")


        choice = int(input("Pick a task to mark complete:"))        
        
        if task_manager.complete_task(choice):
            print("Task marked completed")

    elif choice == "4":
        found = False

        # Print all pending tasks
        print("Pending Tasks")
        for key, task in task_manager.tasks.items():
            if task["task_status"] == "Pending":
                print(f"{key}. {task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")
                found = True

        if not found:
            print("No pending tasks found.")

        found = False
        # Print all completed tasks
        print("Completed Tasks")
        for key, task in task_manager.tasks.items():
            if task["task_status"] == "Completed":
                print(f"{key}. {task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")
                found = True

        if not found:
            print("No completed tasks found.")
    


    elif choice == "5":
        print("Exiting Command Line Task Manager..........")
        break

    else:
        print("Invalid choice!")

    
print(task_manager.tasks)


