import math

class InvalidArgumentException(Exception):
    pass

def calculate_area(width, depth):
    if width < 0 or depth < 0:
        raise InvalidArgumentException('Negative length!!')
    return abs(width * depth)


filename = 'scripts/data.txt'

try:
    with open(filename) as f:
        print(f.read())
        print(10/1)
        print(int('12'))
        getallen = [1,2,3,4]
        print(getallen[3])
        print(calculate_area(18,-3))

except ZeroDivisionError:
    print('Kan niet door 0 delen')

except ValueError:
    print('Geen getal')

except FileNotFoundError:
    print('Bestand is er niet')

except InvalidArgumentException as ex:
    print(ex)
