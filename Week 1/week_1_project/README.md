# CLI Task Manager

A command-line task management application built with Python that allows users to create, track, and manage their daily tasks with persistent JSON storage.

### Overview
This project started as a learning exercise to understand data structures, file handling, and user interaction in Python. Through building this task manager, I encountered several real-world programming challenges that deepened my understanding of dictionaries, JSON operations, and program architecture.

### Features

- Add new tasks with descriptions and due dates
- Remove completed or unwanted tasks
- Mark tasks as complete
- View all tasks in an organized list
- Persistent storage using JSON files

### Technical Implementation

**Data Structure Design**
I chose a nested dictionary structure to store tasks:
pythontasks = {
    1: {
        "task_description": "Complete project",
        "task_due_date": "2024-01-25",
        "task_status": "pending"
    },
    2: {
        "task_description": "Review code",
        "task_due_date": "2024-01-26",
        "task_status": "pending"
    }
}
This structure made JSON serialization straightforward and allowed for easy key-based access to individual tasks.

#### Program Flow

- Load existing tasks from JSON file on startup
- Generate sequential task IDs to maintain ordered keys
- Collect task details from user input (description, due date)
- Set default status to "pending" for all new tasks
- Save changes to JSON file after each operation

#### Challenges & Solutions
**Challenge 1: Task ID Gap Management**
Problem: When users deleted a task, it created gaps in the ID sequence (e.g., {1, 3, 4}). My ID generation logic counted existing tasks and added 1, which caused new tasks to either overwrite existing ones or generate duplicate IDs.

**Solution**: I implemented automatic reordering whenever a task is removed:

- Extract all task values using .values() and store them in a list
- Clear the original dictionary with .clear()
- Loop through the task list and reassign sequential IDs using enumerate()

**Code approach:**
*python# Extract tasks and reorder*
*task_list = list(tasks.values())*
*tasks.clear()*
*for index, task in enumerate(task_list, start=1):*
    *tasks[index] = task*
**Learning:** This challenge taught me how to manipulate dictionary data dynamically and introduced me to useful methods like .keys(), .values(), and .clear().

**Challenge 2: Display Logic Bug**
**Problem:** When showing all tasks to users, my "No tasks found" message kept appearing even when tasks existed.
**Root Cause:** I placed the else statement inside the for loop, so it checked after every iteration instead of after checking all tasks.

**Solution:** I used a boolean flag pattern:
- Initialize a tasks_found variable to False before the loop
- If any task exists, set tasks_found = True
- After the loop completes, check the flag and display "No tasks found" only if still False

**Code approach:**
*pythontasks_found = False*
*for task_id, task in tasks.items():*
    *print(f"Task {task_id}: {task['task_description']}")*
    *tasks_found = True*

*if not tasks_found*
    *print("No tasks found")*
**Learning:** This taught me the importance of loop placement and how to use boolean flags for conditional logic outside loops.

#### Challenge 3: Separation of Concerns
**Problem:** My initial code mixed user interaction (printing messages) with data operations (modifying tasks), making functions harder to reuse and test.
Solution: I refactored to separate responsibilities:

Functions: Return values only, handle data operations
Main program: Handle user interaction and display messages

Example:
*#Function returns data*
def remove_task(tasks, task_id):
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

**Main program handles messaging**
if remove_task(tasks, user_input):
    print("Task removed successfully!")
else:
    print("Task not found")
Learning: This principle made my code more modular and easier to debug, especially when implementing remove_task, show_task, and mark_as_complete functions.

#### Challenge 4: JSON File Operations
Problem: Understanding when and how to save/load data to maintain persistence.

**Solution:**
- Use json.load() at program startup to retrieve existing tasks
- Use json.dump() after every task modification to save changes
- Ensure file handles are properly opened and closed

Learning: This introduced me to file I/O operations and the importance of data persistence in applications. I learned that .load() deserializes JSON to Python objects, while .dump() serializes Python objects to JSON format.
Key Learnings

Dictionary manipulation: Mastered methods like .keys(), .values(), .clear(), and key-based access
Boolean flags: Learned to use flags for controlling program flow outside loops
Code architecture: Understood the value of separating data operations from user interface logic
File handling: Gained practical experience with JSON serialization and persistent storage
Problem-solving approach: Developed a systematic method for debugging - identify the problem, understand the cause, implement a solution, then test thoroughly

## Installation & Usage
**Run the program**
*python task_manager.py*

**Follow the on-screen prompts to:**
1. Add a task
2. View tasks
3. Mark task as complete
4. Remove a task
5. Exit