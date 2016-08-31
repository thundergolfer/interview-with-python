from __future__ import print_function
import unittest

def csv_sort( string , console_out=True):
    items=[x for x in string.split(',')]
    items.sort()
    if console_out:
        print( ','.join(items) )
    else:
        return ','.join(items)



# Unit tests
class csv_sort_tests(unittest.TestCase):

    def setUp(self):
        self.stringOne = "33,44,55,11,22"
        self.stringTwo = "a,f,d,z,y,e"
        self.stringEdge = ""
        self.stringEdgeTwo = "z,z,z,z,z,z,z"

    def test_csv_sort_one(self):
        self.assertEqual(
            csv_sort(self.stringOne, False), "11,22,33,44,55"
        )
        self.assertEqual(
            csv_sort(self.stringTwo, False), "a,d,e,f,y,z"
        )
        self.assertEqual( csv_sort(self.stringEdge, False), "" )
        self.assertEqual(
            csv_sort(self.stringEdgeTwo, False), "z,z,z,z,z,z,z"
        )

if __name__ == '__main__':
    print("Tests started")
    unittest.main()
