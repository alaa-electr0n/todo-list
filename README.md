# todo-list
To Do list programmed by python  
This Python program represents a simple To-Do List application with several functionalities.

## Overview

The application presents a user interface that allows users to manage tasks within the list. It provides the following options:

1. **Add Task**: Add a new task to the list.
2. **Remove a Task**: Remove a specific task from the list.
3. **Mark a Task as Completed**: Mark a task as completed in the list.
4. **Delete All Tasks**: Clear the entire task list.
5. **View the List**: Display all the tasks currently in the list.
6. **Exit the Program**: Terminate the application.

## Functions Overview

### `get_user_action()`
- Requests user input for selecting an action within the range of 1 to 6.
- Validates the user input for the correct range.

### `add_task()`
- Appends a new task to the existing task list.
- Capitalizes the input task name for consistency.

### `remove_one_task()`
- Removes a specific task from the list based on the task number provided by the user.
- Validates the input task number to ensure it exists within the list.
- Handles scenarios where the list is empty or the task number is invalid.

### `mark_one_task()`
- Allows the user to mark a task as completed.
- Displays the tasks for the user to choose from.
- Marks the selected task by appending '✔' at the end of the task name.

### `remove_all_tasks()`
- Clears all the tasks from the list.
- Handles cases where the list is already empty.

### `view_tasks()`
- Displays all tasks in the list along with their respective numbers.
- Handles scenarios where the list is empty.

### `exit_list()`
- Terminates the application and displays a farewell message.

### `using_list()`
- Main loop to continuously prompt the user for actions until they choose to exit.

## Usage
To use the application, execute the code and follow the prompts presented to interact with the To-Do List functionalities.


