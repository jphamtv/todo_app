# Todo App - add, delete, and view tasks.

todo_items = []

def todo_app():
    '''Main loop and user interface for the Todo App'''
    while True:
        if todo_items == []:
            add_task()
        else:
            option = input(
                '\n(a)dd task, (d)elete task, (v)iew list, or e(x)it: '
                )
            option = option.lower()
            if option == 'a':
                add_task()
            elif option == 'd':
                del_task()
            elif option == 'v':
                view_list()
            elif option == 'x':
                print('\nYou have successfully exited the program.')
                break
            else:
                print(f'"{option}" is not a valid option. Please try again.')

def add_task():
    '''Add a task item to the todo list.'''
    add_task = input('\nEnter a task to add: ')
    todo_items.append(add_task)
    print(f'You added {add_task}.')
    view_list()
    
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
        print(f'Task #{task_num} has been deleted')
        view_list()
    except (ValueError, IndexError):
        print('\nThat task # does not exist.')
    
def view_list():
    '''View the todo list.'''
    print(f'\nTodo List:')
    for item in todo_items:
        print(f' - {item}')
    
print('\nTODO LIST APP')
todo_app()