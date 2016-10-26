"""
File: dictionaryBST.py
"""
from arrays import Array
from bst import BST


class BSTHashDict(object):
    """A hashing implementation of a dictionary."""

    DEFAULT_CAPACITY = 3000

    def __init__(self, capacity = None):
        if capacity is None:
            self._capacity = BSTHashDict.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._table = Array(self._capacity)
        for i in xrange(self._capacity):
            self._table[i] = BST()
        self._size = 0

    def __contains__(self, key):
        """Returns True if key is in the dictionary or
        False otherwise."""
        index = abs(hash(key)) % self._capacity 
        return self._table[index].find(key) != None
        

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        index = abs(hash(key)) % self._capacity 
        return self._table[index].find(key)

    def pop(self, key):
        """Removes the entry associated with key and
        returns its value or returns None if key
        does not exist.""" 
        if key in self: 
            self._size -= 1 
            index = abs(hash(key)) % self._capacity 
            return self._table[index].remove(key)
        else:
            return None          

    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        if not key in self: 
            self._size += 1 
        index = abs(hash(key)) % self._capacity 
        self._table[index].add((key, value))

    def __len__(self):
        return self._size

    def __str__(self):
        result = "HashDict: capacity = " +  \
                 str(self._capacity) + ", load factor = " + \
                 str(len(self) / float(self._capacity)) 
        for i in xrange(self._capacity):
            rowStr = ""
            entry = self._table[i]
            # print "row ", i, " ", entry
            rowStr += str(entry) + " "  
            if rowStr != "":
                result += "\nRow " + str(i) + ": " + rowStr
        return result

    def __iter__(self): 
        keys = []
        for i in xrange(self._capacity):
            entry = self._table[i]
            for item in entry:
                keys.append(item)         
        # return iter(sorted(keys)) 
        return iter(keys) 

def main():
    d = BSTHashDict()
    d["Name"] = "Ken"
    d["Age"] = 56
    d["ge"] = 5609
    d["Aoge"] = 560
    d["Agek"] = 156
    d["Agje"] = 586
    print d
    print "Expect True:", "Name" in d
    print "Expect Ken:", d["Name"]
    print "Expect 6:", len(d)
    print "Expect None:", d["Address"]
    d["Age"] = 57
    print "Expect 57:", d["Age"]
    print "Expect Ken:", d.pop("Name")
    print "Expect None:", d.pop("Address")

if __name__ == "__main__": main()
