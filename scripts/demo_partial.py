from functools import partial

def multiply(x:int, y:int, z:int) -> int:
    """Demo Partial"""    
    return x * y * z


partial_multiply = partial(multiply, y=3, z=4)


print(multiply(2,3,4))

print(partial_multiply(2))

settings = {'y':3, 'z':4}
multiply(2, **settings)
multiply(2, y=3, z=4)


settings = [3, 4]
multiply(2, *settings)
