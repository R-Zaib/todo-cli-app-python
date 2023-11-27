import sys

# reference: https://www.pythontutorial.net/python-basics/python-read-text-file/
# the above reference can be used for read 'r', write 'w' and append 'a'

# reference: https://stackoverflow.com/questions/64255055/how-to-use-the-enumerate-function-on-a-txt-file

FILE_PATH = "tasks.txt"
MIN_INDEX_VALUE = 1
MAX_INDEX_VALUE = len("tasks.txt")
ARG_INDEX = sys.argv
ARG_LENGTH = len(ARG_INDEX)
CMD_LIST = "-l"
CMD_ADD = "-a"
CMD_REMOVE = "-r"
CMD_COMPLETE = "-c"

def read_task_file_lines():
    try:
        with open(FILE_PATH, "r") as read_tasks:
            return read_tasks.readlines()
    except FileNotFoundError:
        print("Error! Task file not found. Please create 'tasks.txt' file.")


def write_task_file_lines(lines):
    try:
        with open(FILE_PATH, "w") as w_tasks:
            return w_tasks.writelines(lines)
    except FileNotFoundError:
        print("Error! Task file not found. Please create 'tasks.txt' file.")


def list_tasks():
    tasks = read_task_file_lines()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(i, "-", task)
    else:
        print("No todo tasks for today!")

def add_task(task):
    with open(FILE_PATH, "a") as a_task:
        a_task.write("\n" + task)


# reference: https://datagy.io/python-list-pop-remove-del-clear/ 
def remove_task(index):
    tasks = read_task_file_lines()
    if MIN_INDEX_VALUE < index <= MAX_INDEX_VALUE:
        task_removed = tasks.pop(index - 1)
        write_task_file_lines(tasks)
        print("Removed task: " + task_removed)
    else:
        print("Error! Invalid index, no task was removed.")


def complete_task(index):
    tasks = read_task_file_lines()
    if MIN_INDEX_VALUE < index <= MAX_INDEX_VALUE:
        tasks[index - 1] = u'\u2713' + " " + tasks[index - 1]
        # tasks.insert(-1, u'\u2713')
        write_task_file_lines(tasks)
        print("Marked", index, "as completed.")
    else:
        print("Error! Invalid index, no task was completed.")


def main():
    if ARG_LENGTH == 1:
        print(welcome_message) 
    elif ARG_LENGTH == 2 and ARG_INDEX[1] == CMD_LIST:
        list_tasks()
    elif ARG_LENGTH > 2 and ARG_INDEX[1] == CMD_ADD:
        new_task_to_add = ' '.join(ARG_INDEX[2:])
        if not new_task_to_add:
            print("Error! Unable to add new task, no task given!")   
        else:
            add_task(new_task_to_add)
            print("New task: ", new_task_to_add, "added.")
            list_tasks()
    elif ARG_LENGTH == 3 and ARG_INDEX[1] == CMD_REMOVE:
        index_to_remove = int(ARG_INDEX[2])
        if not index_to_remove:
            print("Error: No task index was entered to remove task.")
        else:
            remove_task(index_to_remove)
            list_tasks()
    elif ARG_LENGTH == 3 and ARG_INDEX[1] == CMD_COMPLETE:
        task_index_to_complete = int(ARG_INDEX[2])
        if not task_index_to_complete:
            print("Error! No task index was entered to complete task.")
        else:
            complete_task(task_index_to_complete)
            list_tasks()
    else:
        print("Error! Enter the correct arguments.")

welcome_message = """
Welcome to To Do List App!

==============================

Command-line arguments:

-l Lists all the tasks

-a Adds a new task

-r Removes a task

-c Completes a task
"""

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Error! Please enter the correct value")    
    except Exception as e:
        print(f"An error occurred. Error type: {e}")

    




# print(u'\u2713')      # sign for completed/checkmark

# click library for handling command line 
# argparse is also good for it
