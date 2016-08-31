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
    return fizzbuzz.rstrip() # remove trailing whitespace


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
        if fizz and buzz:   result.append('fizzbuzz')
        elif fizz:          result.append('fizz')
        elif buzz:          result.append('buzz')
        else:               result.append(i)
    return result


# Unit testing
class fizz_buzz_tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_fizz_buzz_one(self):
        self.assertEqual(
            fizz_buzz_one(0, 12), "fizzbuzz 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz"
        )
        self.assertEqual(fizz_buzz_one(0, 0), "fizzbuzz")
        self.assertEqual(fizz_buzz_one(14,16), "14 fizzbuzz 16")

    def test_fizz_buzz_two(self):
        self.assertEqual(
            fizz_buzz_two(5, 12), ['buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz']
        )
        self.assertEqual(
            fizz_buzz_two(5, -2), []
        )

    def test_fizz_buzz_three(self):
        self.assertEqual(
            fizz_buzz_three(5, 12), ['buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz']
        )

    def test_fizz_buzz_four(self):
        self.assertEqual(
            fizz_buzz_four(5, 12), ['buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz']
        )


if __name__ == '__main__':
    unittest.main()
