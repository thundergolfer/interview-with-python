from future import print_function
import unittest

def csv_sort( string ):
    items=[x for x in input().split(',')]
    items.sort()
    print( ','.join(items) )
