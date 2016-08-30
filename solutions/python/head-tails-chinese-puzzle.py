import unittest

def solve_heads_tails( numheads, numlegs ):
    ns = 'No Solutions!'
    for i in range(numheads+1): # Using a loop to iterate all possible solutions
        j = numheads - i
        if 2*i+4*j == numlegs:
            return i, j
    return ns, ns
