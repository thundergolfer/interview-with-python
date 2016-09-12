import unittest

class ArrayList(object):

    def __init__(self):
        self.list = [0] * 100   # init zeros in each cell
        self.numElems = 0       # list starts empty

    def append(self, x):
        # check if there's enough room
        if self.numElems >= len(self.list):
            self._double_size()
        self.list[self.numElems] = x
        self.numElems += 1

    def pop(self):
        popped = self.list[-1]
        self.list[-1] = 0
        return popped

    def insert(self, index, item):
        if self.numElems == len(self.list):
            self._double_size()
        for i in range(self.numElems, index, -1):
            self.list[i] = self.list[i-1]
        self.list[index] = item

    def _double_size(self):
        # allocate a bigger internal list
        newList = [0] * (2 * len(self.list))
        # copy all the elements from the old list
        i = 0
        for i in range(len(self.list)):
            newList[i] = self.list[i]
        self.list = newList

    def __str__(self):
        s = ""
        for i in range(self.numElems):
            s += str(self.list[i])
            if i != self.numElems: s += ','
        return s



class Test_ArrayList(unittest.TestCase):

    def setUp(self):
        pass

    def test_arraylist_one(self):
        pass


if __name__ == '__name__':
    unittest.main()
