import sys

# reference: https://www.pythontutorial.net/python-basics/python-read-text-file/
# the above reference can be used for read 'r', write 'w' and append 'a'

read_tasks = open("tasks.txt", "r")
#   print(read_tasks.readlines())          # only for testing

# reference: https://stackoverflow.com/questions/64255055/how-to-use-the-enumerate-function-on-a-txt-file
def list_tasks():
    tasks = read_tasks.readlines()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(i, task)

def main():
    if len(sys.argv) != 2:
        print("Please enter correct number of arguments")
    elif sys.argv[1] == "-l":
        list_tasks()
    else:
        print("Error! Enter the correct arguments. Use '-l' to list tasks.")


if __name__ == "__main__":
    main()
    

# welcome_message = """
# Welcome to To Do List App!

# ==============================

# Command-line arguments:

# -l Lists all the tasks

# -a Adds a new task

# -r Removes a task

# -c Completes a task
# """

# print(welcome_message)

# list_tasks()      # for testing

# click library for handling command line 
# argparse is also good for it
# functions to create --> add_task, list_tasks, remove_task, complete_task, read_tasks
