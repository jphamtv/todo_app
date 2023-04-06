# todo_app.py - A simple CLI Todo list to add, delete, and view tasks.

import csv
import os.path

# Define the name of the CSV file to store the tasks.
filename = 'todo_list.csv'

def load_tasks():
    '''Load the task items from the CSV file.'''
    tasks = []
    if os.path.isfile(filename):
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                tasks.append(row[0])
    return tasks

def save_tasks():
    '''Save the task items to the CSV file.'''
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for task in todo_items:
            writer.writerow([task])

# Load the tasks from the CSV file
todo_items = load_tasks()

def todo_app():
    '''Main loop and user interface for the Todo App'''
    while True:
        if not todo_items:            
            add_task()
        else:         
            view_list()   
            option = input(
                '\n(a)dd task, (d)elete task, or e(x)it: '
                )
            option = option.lower()
            if option == 'a':
                add_task()
            elif option == 'd':
                del_task()
            elif option == 'x':
                print('\nExited. Your tasks have been saved.')
                break
            else:
                print(f'"{option}" is not a valid option. Please try again.')

def add_task():
    '''Add a task item to the todo list.'''
    add_task = input('\nEnter a task to add: ')
    todo_items.append(add_task)
    save_tasks()
    print(f'You added {add_task}.')    
    
def del_task():
    '''Delete a task item from the todo list.'''
    print()
    for index, item in enumerate(todo_items):
        print(f'(' + str(index + 1) + ') ' + item)
    task_num = input('\nEnter the task # to delete: ')
    try:
        task_index = int(task_num) - 1
        if task_index < 0 or task_index >= len(todo_items):
            raise IndexError()
        todo_items.pop(task_index)
        save_tasks()
        print(f'Task #{task_num} has been deleted')        
    except (ValueError, IndexError):
        print('\nThat task # does not exist.')
    
def view_list():
    '''View the todo list.'''
    print(f'\nTodo List:')
    for item in todo_items:
        print(f' - {item}')
    
todo_app()