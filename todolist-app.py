import sys

# reference: https://www.pythontutorial.net/python-basics/python-read-text-file/
# the above reference can be used for read 'r', write 'w' and append 'a'

# reference: https://stackoverflow.com/questions/64255055/how-to-use-the-enumerate-function-on-a-txt-file

file_path = "tasks.txt"

def list_tasks():
    with open(file_path, "r") as read_tasks:
        tasks = read_tasks.readlines()
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(i, "-", task)
        else:
            print("No todo tasks for today!")

def add_task(task):
    with open(file_path, "a") as a_task:
        a_task.write("\n" + task)

# def remove_task():
#     

# def complete_task():
#     

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-l":
        list_tasks()
    elif len(sys.argv) > 2 and sys.argv[1] == "-a":
        new_task_to_add = ' '.join(sys.argv[2:])
        if new_task_to_add:
            add_task(new_task_to_add)
            print("New task: ", new_task_to_add, "added.")
            list_tasks()
        else:
            print("Error! Unable to add new task, no task!")   
    else:
        print("Error! Enter the correct arguments.")


if __name__ == "__main__":
    main()
    

welcome_message = """
Welcome to To Do List App!

==============================

Command-line arguments:

-l Lists all the tasks

-a Adds a new task

-r Removes a task

-c Completes a task
"""

print(welcome_message)

# list_tasks()      # for testing

# click library for handling command line 
# argparse is also good for it
# functions to create --> add_task, list_tasks, remove_task, complete_task, read_tasks
