task_list = []

def main():
    proc()

def add_task(task_list,task):
    if task not in task_list:
        task_list.append(task)
        print(f"Your task '{task}' has been added to the list")
    else:
        print(f"Task '{task}' already exists in the list.")

def remove_task(task_list,task):
    if task in task_list:
        task_list.remove(task)
        print(f"Your task '{task}' has been removed from the list")
    else:
        print(f"Task '{task}' is not in the list.")

def view_task(task_list):
    print(f"This is your To-Do list {task_list}")

def proc():
    while True:
        print("\n\t To-Do List \n\n 1.Add task \n 2.Remove Task \n 3.View Task \n 4.Quit\n\n")
        choice = input ("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task_list,task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task_list,task)
        elif choice == "3":
            f"This is your list of tasks {view_task(task_list)}"
        else:
            break
        
        # To - Do Tasks
        
        # Modify Add function to not accept same tasks again
        # Modify Add function to not accept case-differential yet same values
        # Modify remove function to check for values in the list if needed to remove an item which is not part of
        # Modify view function to view as strings but not as lists

if __name__ == '__main__':
  main()

