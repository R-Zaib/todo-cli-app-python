# To do application

### Specification

Create a command-line to do application to easily keep track of your day-to-day tasks.

1. Print usage

Given the terminal opened in the project directory

When the application is run without any arguments

Then it should print the usage information


Example:

$ python todo.py

Command Line To Do Application

==============================

Command-line arguments:

-l Lists all the tasks

-a Adds a new task

-r Removes a task

-c Completes a task

2. List tasks

Given the terminal opened in the project directory

And the file where you store your data

And a task with the description Walk the dog stored in the file

And a task with the description Buy milk stored in the file

And a task with the description Do homework stored in the file

When the application is run with -l argument

Then it should print the tasks that are stored in the file

And it should add numbers before each



Example:

$ todo -l



1 - Walk the dog

2 - Buy milk

3 - Do homework

3. Empty list

Given the terminal opened in the project directory

And the file where you store your data

And the file has 0 task

When the application is run with -l argument

Then it should show a message like this: No todos for today! :)

4. Add new task

Given the terminal opened in the project directory

When the application is run with the -a "Feed the monkey" argument

Then it should add a new task with the description Feed the monkey

5. Add new task error handling

Given the terminal opened in the project directory

When the application is run with the -a argument

Then it should show an error message like: Unable to add: no task provided

6. Remove task

Given the terminal opened in the project directory

And the file where you store your data

And the file has at least 2 tasks

When the application is run with the -r 2 argument

Then it should remove the second task from the file

7. Remove task error handling

case a:

Given the terminal opened in the project directory

When the application is run with the -r argument

Then it should show an error message like: Unable to remove: no index provided

case b:

Given the terminal opened in the project directory

And the file where you store your data

And the file has less than 20 tasks

When the application is run with the -r 20 argument

Then it should show an error message like: Unable to remove: index is out of bound

case c:

Given the terminal opened in the project directory

When the application is run with the -r apple argument

Then it should show an error message like: Unable to remove: index is not a number

8. Argument error handling

Given the terminal opened in the project directory

When the application is run with an unsupported argument (eg. get)

Then it should show an error message like: Unsupported argument

And it should print the usage information

9. Check task

Given the terminal opened in the project directory

And the file where you store your data

And the file has at least 2 tasks

When the application is ran with the -c 2 argument

Then it should check the second task from the file

10. Print all tasks

Given the terminal opened in the project directory

And an undone task with the description Walk the dog stored in the file

And a done task with the description Buy milk stored in the file

And an undone task with the description Do homework stored in the file

When the application is run with -l argument

Then it should print the tasks that are stored in the file

And it should add [ ] before each if its undone otherwise [x]



Example:

1 - [ ] Walk the dog

2 - [x] Buy milk

3 - [ ] Do homework

11. Completion error handling 1: Missing index

Given the terminal opened in the project directory

When the application is run with the -c argument

Then it should show an error message like: Unable to check: no index provided

12. Completion error handling 2: The index is not found

Given the terminal opened in the project directory

And the file where you store your data

And the file has less than 20 tasks

When the application is run with the -c 20 argument

Then it should show an error message like: Unable to check: index is out of bound

13. Completion error handling 3: Invalid argument type

Given the terminal opened in the project directory

When the application is run with the -c apple argument

Then it should show an error message like: Unable to check: index is not a number