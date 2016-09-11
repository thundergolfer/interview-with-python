import unittest

class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def insertStart(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

    def remove(self, elem):
        if self.head == None:
            return False # elem was not found
        elif self.head.cargo == elem:
            self.head = self.head.next
            self.length -= 1
            return True
        else:
            prevNode = self.head
            currNode = self.head.next
        while currNode:
            if currNode.cargo == elem:
                prevNode.next = currNode.next # link over the node to delete
                self.length -= 1
                return True
        return False # elem was not found

    def printBackward(self):
        print("[", end="")
        if self.head != None:
            self.head.printBackward()
        print("]")

class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        if not self.cargo == other.cargo:
            return False
        return True


class Test_LinkedList(unittest.TestCase):

    def setUp(self):
        pass

    def test_linked_list_one(self):
        ll = LinkedList()
        ll.insertStart(5)
        ll.insertStart(10)
        self.assertEqual( ll.length, 2 )
        self.assertTrue( ll.remove(10) )


if __name__ == '__main__':
    unittest.main()
