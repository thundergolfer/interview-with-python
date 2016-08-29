"""solutions to the fibonacci problem"""

def fibonacci_iterative(limit):
    """fibonacci sequence using an iterative approach."""

    a, b = 0, 1
    for i in xrange(limit):
        a, b = b, a + b

    return a

def fibonacci_recursive(limit):
    """fibonacci sequence using a recusive approach."""

    if limit <= 1:
        return limit

    return fibonacci_recursive(limit - 1) + fibonacci_recursive(limit - 2)

def fibonacci_reduce(limit):
    """fibonacci sequence using reduce (shortest option)."""

    return reduce(lambda x, y: x + [x[y] + x[y - 1]], range(1, limit), [0, 1])[-1]

def fibonacci_comprehension(limit):
    """fibonacci sequence using a list comprehension."""

    sequence = [0, 1]

    [sequence.append(sequence[i] + sequence[i-1]) for i in range(1, limit)]

    return sequence[-1]

def fibonacci_generator():
    """ fibonacci sequence using a generator."""
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, b + a
        yield b

if __name__ == '__main__:'

    # Use generator version
    for i,value in zip(range(15),fibonacci_generator()):
        print(value)

    # Cant use this way. You will just get 0's
    for _ in range(15):
        print(next(fibonacci_generator())) # we just keep hitting the first "yeild a"
