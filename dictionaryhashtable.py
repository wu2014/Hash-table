"""
File: dictionaryhashtable.py

"""

from arrays import Array

class Entry(object):
    """A key/value pair."""
    
    def __init__(self, key, value):
        self.key = key
        self.value = value

    # def __eq__(self, other):
    #     return self.key == other.key

    def __str__(self):
        return "(" + str(self.key) + ":" + str(self.value) + ")"

class HashTableDict(object):
    """A hashing implementation of a dictionary."""

    EMPTY = Entry(None,None)
    DELETED = True

    def __init__(self, capacity = 3000,
                 hashFunction = hash,
                 linear = True):
        self._table = Array(capacity, HashTableDict.EMPTY)
        self._size = 0
        self._hash = hashFunction
        self._homeIndex = -1
        self._actualIndex = -1
        self._linear = linear
        self._probeCount = 0

    def __setitem__(self, key,value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        self._probeCount = 0
        # Get the home index
        self._homeIndex = abs(self._hash(key)) % len(self._table)
        distance = 1
        index = self._homeIndex
        if key in self:
            value,index = self.search(key)
        else:    
            # Stop searching when an empty cell is encountered
            while not self._table[index] in (HashTableDict.EMPTY,
                                             HashTableDict.DELETED):

                # Increment the index and wrap around to first 
                # position if necessary
                if self._linear:
                    increment = index + 1
                else:
                    # Quadratic probing
                    increment = self._homeIndex + distance ** 2
                    distance += 1
                index = increment % len(self._table)
                self._probeCount += 1

        # An empty cell is found, so store the item
        self._table[index] = Entry(key,value)
        self._size += 1
        self._actualIndex = index

    def search(self, key):
        """Search for item in the table."""
        self._probeCount = 0
        # Get the home index
        self._homeIndex = abs(self._hash(key)) % len(self._table)
        distance = 1
        index = self._homeIndex
        
        # Stop searching when an empty cell is encountered
        while not self._table[index].key in (HashTableDict.EMPTY,
                                         key):

            # Increment the index and wrap around to first 
            # position if necessary
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        # An empty cell is found, so return None
        if self._table[index] == HashTableDict.EMPTY:
            return None,None
        else:
            self._actualIndex = index
            return self._table[index].value,index

    # Methods __len__(), __str__(), loadFactor(), homeIndex(),
    # actualIndex(), and probeCount() are exercises.
    def __getitem__(self,key):  
        '''Returns the value associated with key or returns None if key does not exist.'''
        return self.search(key)[0]

    def __len__(self):
        return self._size

    def __str__(self):
        result = "HashtableDict:  "         
        for entry in self._table:
            if entry != None: 
                result += str(entry) + " "
        return result

    def loadFactor(self):
        return float(self._size)/len(self._table)

    def homeIndex(self):
        return self._homeIndex

    def actualIndex(self):
        return self._actualIndex

    def probeCount(self):
        return self._probeCount

    def __iter__(self): 
        keys = []
        for entry in self._table:
            if entry.key != None:
                keys.append(entry.key)   
        return iter(keys) 
        # return iter(sorted(keys)) 


    def keys(self): 
        keys = []
        for entry in self._table:
            if entry.key != None:
                keys.append(entry.key)   
        return keys           
    
               
def main():
    tree = HashTableDict()
    
    tree['G'] = 6
    tree['H'] = 16
    tree['A'] = 60
    tree['C'] = 160
    tree['C'] = 36
    tree['E'] = 3
    tree['F'] = 50
    tree['J'] = 5
    tree['J'] = 15
    
    print "\nTree:\n" + str(tree)

   
    print "Find:", " -> ", tree.__getitem__('A')
    print "Find:", " -> ", tree['C']
    print "\nTree:\n" + str(tree)
    print "------------------------- "
    for item in tree:
        print item,


if __name__ == "__main__":
    main()
    



        



