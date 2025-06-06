import random

def random_order1(numbers):
    numbers = numbers.copy()
    random.shuffle(numbers)
    return numbers


def random_order2(numbers):
    numbers = numbers.copy()
    random.shuffle(numbers)
    for number in numbers:
        yield number


numbers = list(range(10))
print(numbers)

numbers = random_order1(numbers)
print(numbers)

for number in random_order2(numbers):
    print(number)
