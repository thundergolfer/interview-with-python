import unittest
from collections import Counter

def count_characters_one( string ):
    """ Counts with a for loop and a dict. """
    d = {}
    for s in string:
        d[s] = d.get(s,0)+1
    return d

def count_characters_two( string ):
    """ Counts using collections.Count """
    counter = Counter(string)
    return counter

    
