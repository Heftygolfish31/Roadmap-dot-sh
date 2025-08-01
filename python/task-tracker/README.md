# Roadmap-dot-sh: Python: Trask Tracker

This is [Task Tracker](/python/task-tracker/README.md) ([link](https://roadmap.sh/projects/task-tracker)), a project that gets you to build a task tracker.

## Requirements

- Add Task.
- Update Task.
- Delete Task.
- Mark Tasks as *In-Progress*.
- Mark Tasks as *Done*.
- List all Tasks.
- List all Tasks that are done.
- List all Tasks that are not done.
- List all Tasks that are in progress.
- Store the data to the project in a JSON file.

## Structure

All user input is taken at the command line level as an argument to the program's execution. The commands are as follows:

- `help`
    - Tell the user how to use the program.

- `version`
    - Tell the user what version of the program they are running.

- `add <DESC>`
    - Adds a Task with the Description specified as a string where `<DESC>` would be.
    - Add also assigns the Task an `ID`, a `status`, a `createdAt` attribute, and a `updatedAt` attribute and stores it in the JSON file.

- `update <ID> <DESC>`
    - Updates the Task with the ID which correlates to the integer ID where `<ID>` would be with the string supplied in place of `<DESC>` (as in add).
    - This maintains the Task's ID but changes it's Description and it's `updatedAt` attribute.

- `delete <ID>`
    - Deletes the Task with the ID which correlates to the integer ID where `<ID>` would be.
    - This ID is never reused.
    
- `mark-in-progress <ID>`
    - Marks the Task with the target ID specified in `<ID>` as `in-progress`, updating it's `updatedAt` and `status` attributes accordingly.

- `mark-done <ID>`
    - Marks the Task with the target ID specified in `<ID>` as `done`, updating it's `updatedAt` and `status` attributes accordingly.

- `list`
- `list <done|todo|in-progress|>`
    - List all Tasks.
    - If an argument of either `done`, `to-do`, or `in-progress` is specified, only Tasks with that value in their `status` attribute will be listed.

## Process

- `TASK-1`: Take Arguments.
- `TASK-2`: Switch Mode Depending On Arguments Given.
- `TASK-3`: Add 'Add' Functionality.
- `TASK-4`: Detect And Catch 'And' Errors.
- `TASK-5`: Add 'Update' Functionality.
- `TASK-6`: Detect And Catch 'Update' Errors.
- `TASK-7`: Add 'Delete' Functionality.
- `TASK-8`: Detect And Catch 'Delete' Errors.
- `TASK-9`: Add 'Marking' Functionality.
- `TASK-10`: Detect And Catch 'Marking' Errors.
- `TASK-11`: Add 'List' Functionality.
- `TASK-12`: Detect And Catch 'List' Errors.
- `TASK-13`: Add 'Help' Functionality.
- `TASK-14`: Add 'Version' Functionality.
- `TASK-15`: Clean-up.