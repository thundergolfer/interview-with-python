from future import print_function
import unittest

def dict_of_squared_int( number ):
    """ Using a regular for loop. """
    n=int(input())
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i

    print( d )

def dict_of_squared_int_two( number ):
    """ Using a dictionary comprehension. """
    n=int(input())
    d = { i: i*i for i in range(1, n+1)}

    print( d )
