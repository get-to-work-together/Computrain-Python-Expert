import logging
import math
import time


logging.basicConfig(
    filename = 'debug.log',
    level = logging.WARNING
)

def debug(f):
    def wrapper(*args, **kwargs):
        logging.warning(f'Calling function: {f.__name__}({', '.join(map(str, args))})')
        t0 = time.time_ns()
        return_value = f(*args, **kwargs)
        t1 = time.time_ns()
        delta_t = t1 - t0
        logging.warning(f'Done in {delta_t} ns')
        return return_value
    return wrapper


@debug
def calculate_something(x):
    return math.log10(x * x * x)


for x in range(1, 100):
    print(f'{x:<8} : {calculate_something(x)}')
