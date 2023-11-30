import sys

FILE_PATH = "tasks.txt"
MIN_INDEX_VALUE = 1
ARG_COMMAND = sys.argv
ARG_LENGTH = len(ARG_COMMAND)
CMD_LIST = "-l"
CMD_ADD = "-a"
CMD_REMOVE = "-r"
CMD_COMPLETE = "-c"
WELCOME_MESSAGE = """
Welcome to To Do List App!

This To-Do List App allows you to manage your day-to-day tasks using the command line.
You can add, remove, complete and list tasks conveniently.
You can use the command-line arguments to do so.

==============================

Command-line arguments:

-l Lists all the tasks

-a Adds a new task

-r Removes a task

-c Completes a task
"""


def read_task_file_lines():
    # reference: https://www.pythontutorial.net/python-basics/python-read-text-file/
    """
    read the lines from the tasks file and return a list of tasks
    returned list: a list containing the tasks read from the file with removed whitespaces
    if the tasks.txt file is not found, it raises FileNotFoundError
    """
    try:
        tasks_todo_list = []
        with open(FILE_PATH, "r") as read_tasks:
            for row in read_tasks:
                r = row.strip()
                if r:
                    tasks_todo_list.append(r)    
        return tasks_todo_list
    except FileNotFoundError:
        print("Error! Task file not found. Please create 'tasks.txt' file.")


def write_task_file_lines(lines):
    """
    write the given lines to the tasks file using parameter "lines"
    if the tasks.txt file is not found, it raises FileNotFoundError
    if any other error occurs during the writing process, it prints the error type
    """
    try:
        with open(FILE_PATH, "w") as w_tasks:
            w_tasks.write("\n".join(lines))
    except FileNotFoundError:
        print("Error! Task file not found. Please create 'tasks.txt' file.")
    except Exception as e:
        print("An error occurred. Error type: ",e)


def list_tasks():
    # reference: https://stackoverflow.com/questions/64255055/how-to-use-the-enumerate-function-on-a-txt-file
    """
    list all the tasks from the tasks file and print them using the format "<index> - <task>"
    if there are no tasks, it prints "No todo tasks for today!"
    """
    tasks = read_task_file_lines()
    if tasks:
        for i, task in enumerate(tasks, MIN_INDEX_VALUE):
            print(i, "-", task)
    else:
        print("No todo tasks for today!")


def add_task(task):
    # reference: https://sparkbyexamples.com/python/python-remove-a-trailing-new-line/
    """
    add a new task to the tasks file using "task" parameter as string
    if the tasks.txt file is not found, it raises FileNotFoundError
    if any other error occurs during the add process, it prints the error type
    """
    try:
        with open(FILE_PATH, "a") as a_task:
            a_task.write("\n" + "[ ] " + task.rstrip())
    except FileNotFoundError:
        print("Error! Task file not found. Please create 'tasks.txt' file.")
    except Exception as e:
        print("An error occurred. Error type: ",e)


def remove_task(index):
    # reference: https://datagy.io/python-list-pop-remove-del-clear/ 
    # reference: https://stackoverflow.com/questions/60607645/replacing-characters-by-chaining-str-replace-methods-produces-wrong-result
    """
    remove a task from the tasks file based on the given index (int) as its parameter
    it prints the removed task
    if the index is out of range, it gives an error to the user
    """
    tasks = read_task_file_lines()
    if tasks and MIN_INDEX_VALUE <= index <= len(tasks):
        task_removed = tasks.pop(index - 1)
        write_task_file_lines(tasks)
        print_removed_task = task_removed.replace("[ ] ", "").replace("[\u2713]", "")
        print("Removed task: " + print_removed_task)
    else:
        print("Error! Invalid index, no task was removed.")


def complete_task(index):
    # reference: https://stackoverflow.com/questions/41079054/how-does-python-startswith-work
    """
    complete a task from the tasks file based on the given index (int) as its parameter
    adds a tick mark in the square bracket to indicate that the task is marked as completed
    it prints the completed task
    if task was previously marked as completed, it gives an error that the task was marked already
    if the index is out of range, it gives an error to the user
    """
    tasks = read_task_file_lines()
    if tasks and MIN_INDEX_VALUE <= index <= len(tasks):
        i = index - 1
        if "[\u2713] " in tasks[i]:
            print("Task", index, "is already marked as completed.")
        elif "[ ]" in tasks[i]:
            tasks[i] = tasks[i].replace("[ ] ", "[\u2713] ", 1)
            write_task_file_lines(tasks)
            print("Marked", index, "as completed.")
    else:
        print("Error! Invalid index, no task was completed.")


def main():
    """
    the main function for the to-do list CLI app
    handles the command-line arguments and executes corresponding actions
    prints welcome message or error messages based on user input
    if there is an issue with the provided command-line arguments it raises ValueError
    """
    if ARG_LENGTH == 1:
        print(WELCOME_MESSAGE) 
    elif ARG_LENGTH == 2 and ARG_COMMAND[1] == CMD_LIST:
        list_tasks()
    elif ARG_LENGTH >= 2 and ARG_COMMAND[1] == CMD_ADD:
        new_task_to_add = ' '.join(ARG_COMMAND[2:])
        if not new_task_to_add:
            print("Error! Unable to add new task, no task given!")   
        else:
            add_task(new_task_to_add)
            print("New task: ", new_task_to_add, "added.")
    elif ARG_LENGTH == 2 and ARG_COMMAND[1] == CMD_REMOVE:
        print("Error: No task index was entered to remove task.")
    elif ARG_LENGTH == 3 and ARG_COMMAND[1] == CMD_REMOVE:
        try:
            index_to_remove = int(ARG_COMMAND[2])
            remove_task(index_to_remove)
        except ValueError:
            print("Error: Task index must be an integer.")
    elif ARG_LENGTH == 2 and ARG_COMMAND[1] == CMD_COMPLETE:
        print("Error! No task index was entered to complete task.")
    elif ARG_LENGTH == 3 and ARG_COMMAND[1] == CMD_COMPLETE:
        try:
            task_index_to_complete = int(ARG_COMMAND[2])
            complete_task(task_index_to_complete)
        except ValueError:
            print("Error: Task index must be an integer.")
    else:
        print("Error! Enter the correct arguments.")
        print(WELCOME_MESSAGE)


if __name__ == "__main__":
    try:
        main()
        """
        execute the main function and handle specific exceptions

        ValueError: If there is an issue with the provided command-line arguments
        Exception: If any other error occurs during the execution, it prints the error type
        """
    except ValueError:
        print("Error! Please enter the correct value")    
    except Exception as e:
        print("An error occurred. Error type: ",e)
