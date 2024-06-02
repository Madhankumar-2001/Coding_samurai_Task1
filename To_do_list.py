import os

TASKS_FILE = "tasks.txt"

class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nCompleted: {status}\n"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)

    def mark_task(self, task_id, completed):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = completed
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.renumber_tasks()
                self.save_tasks()
                return True
        return False

    def renumber_tasks(self):
        for i, task in enumerate(self.tasks):
            task.task_id = i + 1

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            for task in self.tasks:
                file.write(f"ID: {task.task_id}\nTitle: {task.title}\nDescription: {task.description}\nCompleted: {'✔' if task.completed else '✘'}\n\n")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                task_data = file.read().strip().split("\n\n")
                for task_str in task_data:
                    if task_str.strip():
                        task_lines = task_str.split("\n")
                        if len(task_lines) >= 4:
                            task_id = int(task_lines[0].split(": ")[1])
                            title = task_lines[1].split(": ")[1]
                            description = task_lines[2].split(": ")[1]
                            completed = task_lines[3].split(": ")[1] == "✔"
                            task = Task(task_id, title, description, completed)
                            self.tasks.append(task)

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Mark Task as Incomplete")
    print("5. Delete Task")
    print("6. Exit")

def main():
    manager = TaskManager()
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
            print("Task added successfully.")
        
        elif choice == '2':
            manager.list_tasks()
        
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            if manager.mark_task(task_id, True):
                print("Task marked as completed.")
            else:
                print("Task ID not found.")
        
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as incomplete: "))
            if manager.mark_task(task_id, False):
                print("Task marked as incomplete.")
            else:
                print("Task ID not found.")
        
        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            if manager.delete_task(task_id):
                print("Task deleted successfully.")
            else:
                print("Task ID not found.")
        
        elif choice == '6':
            print("Exiting the application. ThankYou! :)")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

