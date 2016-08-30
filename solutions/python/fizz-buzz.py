""" Implementations of the class Fizz-Buzz problem """

import unittest # TODO: 


def fizz_buzz_one( start, end ):
    fizzbuzz = ''
    for i in range(start,end+1):
        if i%3 == 0:
            fizzbuzz += "fizz"
        if i%5 == 0:
            fizzbuzz += "buzz"
        if i%3 != 0 and i%5 != 0:
            fizzbuzz += str(i)

        fizzbuzz += ' '
    print(fizzbuzz)


def fizz_buzz_two( start, end ):
    fizzbuzz = []
    for i in range(start,end+1):
        entry = ''
        if i%3 == 0:
            entry += "fizz"
        if i%5 == 0:
            entry += "buzz"
        if i%3 != 0 and i%5 != 0:
            entry = i

        fizzbuzz.append(entry)

    for i in fizzbuzz:
        print(i)

def fizz_buzz_three( start, end ):
    def int_to_fizzbuzz(i):
        """ Utility function for fizzbuzz_three. """
        entry = ''
        if i%3 == 0:
            entry += "fizz"
        if i%5 == 0:
            entry += "buzz"
        if i%3 != 0 and i%5 != 0:
            entry = i
        return entry
    return [int_to_fizzbuzz(i)  for i in range(start, end+1)]
