class Task:
    def __init__(self, title):
        ''' Initializes a Task object with a title'''
        self.title = title
        self.completed = False

    def mark_complete(self):
        ''' Marks the task as completed '''
        self.completed = True

    def __str__(self):
        ''' Returns a string representation of the task '''
        status = "Complete" if self.completed else "Incomplete"
        return f"{self.title} - {status}"


class ToDoList:
    def __init__(self):
        ''' Initializes a ToDoList object '''
        self.tasks = []

    def add_task(self, title):
        ''' Adds a task to the list '''
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def view_tasks(self):
        ''' Prints out all tasks in the list '''
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def mark_task_complete(self, task_index):
        ''' Marks a task as completed '''
        try:
            task = self.tasks[task_index - 1]
            task.mark_complete()
            print(f"Task '{task.title}' marked as complete.")
        except IndexError:
            print("Error: Task index out of range.")

    def delete_task(self, task_index):
        ''' Deletes a task from the list '''
        try:
            task = self.tasks.pop(task_index - 1)
            print(f"Task '{task.title}' deleted.")
        except IndexError:
            print("Error: Task index out of range.")

def display_menu():
    '''  Displays the main menu '''
    print("\nWelcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            try:
                task_index = int(input("Enter task number to mark as complete: "))
                todo_list.mark_task_complete(task_index)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '4':
            try:
                task_index = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_index)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '5':
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Error: Invalid option. Please select a number between 1 and 5.")

main()