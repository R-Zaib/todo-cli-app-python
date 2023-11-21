import sys

# reference: https://www.pythontutorial.net/python-basics/python-read-text-file/
# the above reference can be used for read 'r', write 'w' and append 'a'

# reference: https://stackoverflow.com/questions/64255055/how-to-use-the-enumerate-function-on-a-txt-file

file_path = "tasks.txt"
MIN_INDEX_VALUE = 1
MAX_INDEX_VALUE = len("tasks.txt")

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

# reference: https://datagy.io/python-list-pop-remove-del-clear/ 
def remove_task(index):
    with open(file_path, "r") as read_tasks:
        tasks = read_tasks.readlines()
    if MIN_INDEX_VALUE < index <= MAX_INDEX_VALUE:
        task_removed = tasks.pop(index - 1)

        with open(file_path, "w") as w_tasks:
            w_tasks.writelines(tasks)
        
        print("Removed task: " + task_removed)
    else:
        print("Error! Invalid index, no task was removed.")


def complete_task(index):
    with open(file_path, "r") as read_tasks:
        tasks = read_tasks.readlines()
    if MIN_INDEX_VALUE < index <= MAX_INDEX_VALUE:
        tasks[index - 1] = u'\u2713' + " " + tasks[index - 1]
        # tasks.insert(-1, u'\u2713')

        with open(file_path, "w") as w_task:
            w_task.writelines(tasks)

        print("Marked", index, "as completed.")
    else:
        print("Error! Invalid index, no task was completed.")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-l":
        list_tasks()
    elif len(sys.argv) > 2 and sys.argv[1] == "-a":
        new_task_to_add = ' '.join(sys.argv[2:])
        if not new_task_to_add:
            print("Error! Unable to add new task, no task given!")   
        else:
            add_task(new_task_to_add)
            print("New task: ", new_task_to_add, "added.")
            list_tasks()
    elif len(sys.argv) == 3 and sys.argv[1] == "-r":
        index_to_remove = int(sys.argv[2])
        if not index_to_remove:
            print("Error: No task index was entered to remove task.")
        else:
            remove_task(index_to_remove)
            list_tasks()
    elif len(sys.argv) == 3 and sys.argv[1] == "-c":
        task_index_to_complete = int(sys.argv[2])
        if not task_index_to_complete:
            print("Error! No task index was entered to complete task.")
        else:
            complete_task(task_index_to_complete)
            list_tasks()
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

# print(welcome_message)
# print(u'\u2713')      # sign for completed/checkmark

# click library for handling command line 
# argparse is also good for it
