def print_todo(todo):
    """
    Print todo takes in the todo and prints it out.
    with by seperating the 'name' from the 'body' using a colon (:).

    >>> todo = ('name': 'Example 1', 'body': 'This is a test task', 'points': '3')
    >>> print_todo(todo)
    Example 1: This is a test task
    >>>
    """
    print(f"{todo['name']}: {todo['body']}")

def take_first(todos):
    """
    take_first receives a list of todos and removes the first todo
    and returns that todo and the remaing todos in a touple

    >>> todos = [{'name': "Example 1', 'body': "This is a test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    >>> todo, todos = take_first(todos)
    >>> todo
    {'name': "Example 1', 'body': "This is a test task', 'points': '3'}
    >>> todo
    [{'name': 'Task 2'. 'body': 'Yet another example task', 'points': '2'}]
    """
    todo = todos.pop(0)
    return (todo, todos)

def sum_points(todo1, todo2):
    """
    sum_points recieves the todo dictionaries and returns the sum of their 'point' values.

    >>>   todos = [{'name': 'Example 1', 'body': 'This is a test task', 'point': '3'},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    >>> sum_points(todos[0], todos[1])
    5
    """

    return int(todo1['points']) + int(todo2['points'])
