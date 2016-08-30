""" Implementations of the class Fizz-Buzz problem """

import unittest # TODO:


def fizz_buzz_one( start, end ):
    """ Note: This method returns a long string not a list. """
    fizzbuzz = ''
    # range is NOT inclusive of the 2nd number, so add 1 to include it.
    # range(1,4) > 1,2,3. range(1, 4 + 1) > 1,2,3,4.
    for i in range(start,end+1):
        if i%3 == 0:
            fizzbuzz += "fizz"
        if i%5 == 0:
            fizzbuzz += "buzz"
        if i%3 != 0 and i%5 != 0:
            fizzbuzz += str(i)

        fizzbuzz += ' '
    return fizzbuzz


def fizz_buzz_two( start, end ):
    fizzbuzz = []
    for i in range(start,end+1):
        entry = '' # initialsing an empty string
        if i%3 == 0:
            entry += "fizz" # concatenating "fizz" to string
        if i%5 == 0:
            entry += "buzz"
        if i%3 != 0 and i%5 != 0:
            # this is dynamic typing. reassigning a prev. string to int
            entry = i
        fizzbuzz.append(entry) # stick entry onto end of list
    return fizzbuzz

def fizz_buzz_three( start, end ):
    """
    Returns the fizzbuzz string for a given range using an inner
    function and a list comprehension.
    """
    def int_to_fizzbuzz(i):
        """ Output the 'fizzbuzz' string for a single number. """
        entry = ''
        if i%3 == 0: # if i divided by 3 has no remainder
            entry += "fizz"
        if i%5 == 0: # if i divided by 5 has no remainder
            entry += "buzz"
        if i%3 != 0 and i%5 != 0: # i is not divisible by 3 or 5 without remainder
            entry = i
        return entry
    return [int_to_fizzbuzz(i)  for i in range(start, end+1)]

def fizz_buzz_four( start, end ):
    """
    Fizz buzz showing compact if-elif-else form,
    and precalculatio of boolean values.
    """
    result = [] # initalising a list to hold our result
    for i in range(start, end+1):
        fizz = (i % 3 == 0)
        buzz = (i % 5 == 0)
        if fizz and buzz:   result.append('Fizzbuzz')
        elif fizz:          result.append('Fizz')
        elif buzz:          result.append('Buzz')
        else:               result.append(i)
    return result
