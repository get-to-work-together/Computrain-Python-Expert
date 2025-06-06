def my_decorator(f):
    def wrapper(*args, **kwargs):
        print(f'Calling function: {f.__name__}')
        print(f'Positional arguments: {args}')
        return_value = f(*args, **kwargs)
        print('Done')
        return return_value
    return wrapper


@my_decorator
def my_function(name='stranger'):
    print(f'Hello {name}')


my_function()
my_function('Everybody')