"""Demo type hinting"""

n: int = 123

# n = '123'

print(type(n))

def doe_iets_anders(x: int|float, y: int) -> list[int|float]:
    """Doe iets"""
    return [x] * y

print( doe_iets_anders(3, 5) )
