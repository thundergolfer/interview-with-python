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
    def __init__(self):
        self.size = 11
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
