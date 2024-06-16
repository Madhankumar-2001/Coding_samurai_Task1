# Coding_samurai_Task1
Creating a To-Do-List taks using python.

PROJECT DESCRIPTION: 
  This project is a simple command-line to-do list application in Python, designed to help users manage their tasks efficiently. It allows users to add, list, mark as complete/incomplete, and delete tasks, with task persistence achieved through a text file.

### How to Run

1. Clone the Repository: 
   git clone (repository-url)
   cd (repository-directory)
   

2. Run the Application:
   python (filename).py

### Code Explanation

1. **Imports and File Constants:**
   - `import os`: For checking the existence of the tasks file.
   - `TASKS_FILE = "tasks.txt"`: The file where tasks are stored.

2. **Task Class:**
   - `class Task`: Defines the structure of a task.
   - `__init__(self, task_id, title, description, completed=False)`: Initializes a task with an ID, title, description, and completion status.
   - `__str__(self)`: Returns a string representation of the task.

3. **TaskManager Class:**
   - `class TaskManager`: Manages the collection of tasks.
   - `__init__(self)`: Initializes the task manager and loads tasks from the file.
   - `add_task(self, title, description)`: Adds a new task to the list and saves the updated list to       the file.
   - `list_tasks(self)`: Lists all tasks, printing them to the console.
   - `mark_task(self, task_id, completed)`: Marks a task as completed or incomplete based on its ID.
   - `delete_task(self, task_id)`: Deletes a task by its ID and renumbers the remaining tasks.
   - `renumber_tasks(self)`: Renumbers tasks to ensure continuity after deletions.
   - `save_tasks(self)`: Saves the current list of tasks to the file.
   - `load_tasks(self)`: Loads tasks from the file if it exists.

4. **Menu Display Function:**
   - `def display_menu()`: Prints the menu options for the user.

5. **Main Function:**
   - `def main()`: The main loop of the application.
   - Initializes a `TaskManager` instance.
   - Continuously displays the menu and processes user input:
     - `1. Add Task`: Prompts for task details and adds the task.
     - `2. List Tasks`: Lists all tasks.
     - `3. Mark Task as Completed`: Marks a task as completed based on user input.
     - `4. Mark Task as Incomplete`: Marks a task as incomplete based on user input.
     - `5. Delete Task`: Deletes a task based on user input.
     - `6. Exit`: Exits the application.

### Features

- **Add Task:** Allows users to add tasks with a title and description.
- **List Tasks:** Displays all tasks with their details.
- **Mark Task as Completed/Incomplete:** Updates the completion status of tasks.
- **Delete Task:** Removes a task from the list.
- **Persistent Storage:** Saves and loads tasks from a text file to maintain state between sessions.

### Usage

1. **Adding a Task:** Enter the task title and description when prompted.
2. **Listing Tasks:** View all current tasks with their statuses.
3. **Marking Tasks:** Change the completion status of a task by entering its ID.
4. **Deleting Tasks:** Remove tasks by their ID.
5. **Exiting:** End the application and save the current state of tasks.
