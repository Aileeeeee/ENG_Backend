# Import JSON library
import json 

# Define variables
tasks = {}
completion_status = "pending"
filename = "my_tasks.json"

# Define a function `add_task` to add task to task manager
def add_task(tasks):
    task_id = len(tasks) + 1
    task_description = input("Enter task description (e.g Buy groceries): ").title()
    task_due_date = input("Enter task due date (DD-MM-YYYY): ")

    task = {"task_description":task_description,"task_due_date":task_due_date,"task_status":completion_status}

    tasks[task_id] = task
    return tasks

# Define a function `mark_task_complete` to mark task completed
def mark_task_complete(tasks,task_id):
     if task_id in tasks:
          return True
     else:
          return False

# Define a function `remove_task` to mark task completed   
def remove_task(tasks,task_id):
    if task_id in tasks:
        del tasks[task_id]

        # Reordering dictionary keys
        all_tasks = list(tasks.values())
        tasks.clear()
        for index,task in enumerate(all_tasks,start=1):
            tasks[index] = task
        return True
    else:
         return False
        
# Define a function `show_tasks` to show all tasks (pending and completed)
def show_tasks(tasks):
    if tasks:
        return True
    else:
        return False

# Define a function `save_to_json` to save tasks to JSON file         
def save_to_json():
    with open (filename,"w") as file:
        json.dump(tasks,file,indent=2)

    return tasks

# Define a function `save_to_json` to save tasks to JSON file 
def load_from_json():
    try:
        with open(filename, "r") as file:
            loaded_tasks = json.load(file)
            return {int(key):value for key,value in loaded_tasks.items()}
    except FileNotFoundError:
        return {}

# Load tasks from JSON file            
tasks = load_from_json()  

# Main program
while True:
        print("\n1. Add task")
        print("2. Mark task complete")
        print("3. Remove task")
        print("4. Show tasks")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
            
        if choice == "1":
            add_task(tasks)
            save_to_json()
            print ("Task added!")

        elif choice == "2":
            if not tasks:
                  print("No tasks exists in the file manager.")
            else:
                for key , task in tasks.items():
                    print(f"{key}. {task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")
                
                mark_choice = int(input("Pick the task you would like to mark complete: "))
                    
                if mark_task_complete(tasks,mark_choice):
                    tasks[mark_choice]["task_status"] = "completed"
                    print(f"Task #{mark_choice} has been marked completed!")
                    save_to_json()
                else:
                     print("Invalid choice. This task does not exist in the task manager!")
                                   
        elif choice == "3":
            for key, task in tasks.items():
                print(f'{key}. {task["task_description"]} - {task["task_due_date"]} - {task["task_status"]} ')

            remove_choice = (int(input("Which task would you like to remove: ")))

            if remove_task(tasks,remove_choice):
                print("Task removed")
                save_to_json()
            else:
              print("Invalid choice. This task does not exist in the task manager")   
   
        elif choice == "4":
                found = False
                print("Pending Tasks: ")
                if show_tasks(tasks):
                    for key, task in tasks.items():
                        if task["task_status"] == "pending":
                            print(f"{task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")
                            found = True
                    if not found:
                        print("No pending tasks.")

                found = False
                print("\nCompleted Tasks: ")
                if show_tasks(tasks):
                    for key, task in tasks.items():
                        if task["task_status"] == "completed":
                            print(f"{task["task_description"]} - {task["task_due_date"]} - {task["task_status"]}")
                            found = True
                            
                    if not found:
                         print("No completed tasks.")
                                       
        elif choice == "5":
                print("Done")
                break
        
        else:
                print("Invalid choice")
