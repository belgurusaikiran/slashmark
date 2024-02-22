class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task[0]} - {'Completed' if task[1] else 'Not Completed'}")

    def add_task(self, task_name):
        self.tasks.append([task_name, False])
        print(f"Task '{task_name}' added to your to-do list.")

    def mark_task_completed(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            self.tasks[task_num - 1][1] = True
            print(f"Task {task_num} marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            del self.tasks[task_num - 1]
            print(f"Task {task_num} removed from your to-do list.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter the task name: ")
            todo_list.add_task(task_name)
        elif choice == '3':
            todo_list.display_tasks()
            task_num = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_num)
        elif choice == '4':
            todo_list.display_tasks()
            task_num = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_num)
        elif choice == '5':
            print("Thank you for using the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
    
