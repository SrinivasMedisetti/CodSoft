class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed!")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")


def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")


def main():
    todo_list = ToDoList()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task name: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task name to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()