import unittest

class HashTable_One(object):

    def __init__(self):
        self.table = [None] * 256

    def _get_value(self, key):
        total = 0
        for i in range(len(key)):
            total += ord(key[i]) * (7**i)
        return (len(key) * total) % 256

    def insert(self, key): # Why starting with a single value and only after that changing to a list? I recommend starting with a list right from the start.
        val = self._get_value(key)
        if self.table[val] == None:
            self.table[val] = key
        else:
            if type(self.table[val]) == list:
                self.table[val].append(key)
            else:
                self.table[val] = [self.table[val], key]

    def delete(self, key):
        val = self._get_value(key)
        if self.table[val] != None:
            if isinstance(self.table[val], list):
                i = self.table[val].index(key)
                self.table[val][i] = None  # use list.remove instead
            else:
                self.table[val] = None
        else:
            raise KeyError("key {key} can't be found.".format(key=key))

    def lookup(self, key):
        found = False
        val = self._get_value(key)
        if type(self.table[val]) == list:
            found = key in self.table[val]
        else:
            found = self.table[val] == key
        return found

class HashTable_Two(object):
    """ from http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html """
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

## HASHTABLE THREE ###
class Node(object):
    def __init__(self, key, value=None, next=None):
        self.key = key
        self.data = value
        self.next  = next


class HashTable_Three(object):

    def __init__(self, size=10):
        self.size = size
        self.slots = [None for i in range(self.size)]

    def put(self, key, data):
        hashVal = self.hash_function(key, self.size)

        if self.slots[hashVal] == None:
            self.slots[hashVal] = Node(key, data)
        elif self.slots[hashVal].key == key:
            self.slots[hashVal].data = data # replace value
        else:
            currNode = self.slots[hashVal].next
            while currNode:
                if currNode.key == key:
                    currNode.data = data # replace value
                    break
                currNode = currNode.next
            else: # couldn't find key in table so add it
                prevNode.next = Node(key, data)

    def get(self, key):
        search_slot = self.hash_function(key, self.size)
        if self.slots[search_slot] == None:
            raise KeyError("'{}' not in table.".format(key))
        elif self.slots[search_slot].key == key: # check head node
            return self.slots[search_slot].data
        else:
            currNode = self.slots[search_slot].next
            while currNode:
                if currNode.key == key:
                    return currNode.data
                currNode = currNode.next
            else: # ran out of nodes
                raise KeyError("{} not in table.".format(key))

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hash_function(self, key, seed=7):
        h = seed
        for c in key:
            h ^= ( ( h << 5) + ord(c) + (h >> 2) )
        return (h & 0x7fffffff) % self.size





class Test_Hashtable(unittest.TestCase):

    def setUp(self):
        pass

    def test_hashtable_one(self):
        pass

    def test_hashtable_three_hashfunction(self):
        ht = HashTable_Three()
        num = ht.hash_function('carrot')
        numtwo = ht.hash_function('carrot')
        self.assertEqual(num , numtwo )

    def test_hashtable_three(self):
        ht = HashTable_Three()
        ht['one'] = 1
        ht['two'] = 2
        self.assertEqual( ht['one'], 1 )
        ht['one'] = 100
        self.assertEqual( ht['one'], 100)


if __name__ == '__main__':
    unittest.main()
