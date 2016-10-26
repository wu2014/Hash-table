"""
File: bst.py
BST class for binary search trees.
"""

from queue import LinkedQueue
from binarytree import BinaryTree

class BST(object):

    def __init__(self):
        self._tree = BinaryTree.THE_EMPTY_TREE
        self._size = 0


    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._tree)

    def __iter__(self):
        return iter(self.inorder())

    def find(self, target):
        """Returns data if target is found or None otherwise."""
        def findHelper(tree):
            if tree.isEmpty():
                return None
            elif target == tree.getRoot()[0]:
                return tree.getRoot()[1]
            elif target < tree.getRoot()[0]:
                return findHelper(tree.getLeft())
            else:
                return findHelper(tree.getRight())
            
        return findHelper(self._tree)

    def add(self, newItem):
        """Adds newItem to the tree."""

        # Helper function to search for item's position 
        def addHelper(tree):
            currentItem = tree.getRoot()
            left = tree.getLeft()
            right = tree.getRight()

            # New item is less, go left until spot is found
            if newItem[0] < currentItem[0]:
                if left.isEmpty():
                    tree.setLeft(BinaryTree(newItem))
                else:
                    addHelper(left)                    

            # New item is greater or equal, 
            # go right until spot is found
            elif newItem[0] == currentItem[0]:
                tree.setRoot(newItem)
            elif right.isEmpty():
                tree.setRight(BinaryTree(newItem))
            else:
                addHelper(right)
            # End of addHelper

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._tree = BinaryTree(newItem)

        # Otherwise, search for the item's spot
        else:
            addHelper(self._tree)
        self._size += 1

    def inorder(self):
        """Returns a list containing the results of
        an inorder traversal."""
        lyst = []
        self._tree.inorder(lyst)
        return lyst


    def preorder(self):
        """Returns a list containing the results of
        a preorder traversal."""
        lyst = []
        self._tree.preorder(lyst)
        return lyst

    def postorder(self):
        """Returns a list containing the results of
        a postorder traversal."""
        lyst = []
        self._tree.postorder(lyst)
        return lyst


    def levelorder(self):
        """Returns a list containing the results of
        a levelorder traversal."""
        lyst = []
        self._tree.levelorder(lyst)
        return lyst

    def lookup(self, data,parent=None):
        def lookupHelper(tree,parent):
            value = tree.getRoot()[0]
            left = tree.getLeft()
            right = tree.getRight()
            if data < value:
                if left is None:
                    return None, None
                if not left.isEmpty():
                    # print data, "->", left.getRoot()
                    return lookupHelper(left,parent)
                else:
                    return None, None
            elif data > value:
                if right is None:
                    return None, None
                if not right.isEmpty():
                    # print data, "->", right.getRoot()
                    return lookupHelper(right,parent)
                else:
                    return None, None
            else:
                return tree, parent
        return lookupHelper(self._tree,parent)

 
    def remove(self, data):
        node, parent = self.lookup(data)
        value = node.getRoot()[1]
        #print n, parent
        if node is None: return None

        left = node.getLeft()
        right = node.getRight()
        children_count = 0
        if not left.isEmpty(): children_count += 1
        if not right.isEmpty(): children_count += 1
        #print "children_count: ", children_count
        if children_count == 0:
            if parent is not None:
                if parent.getLeft() == node:
                    parent.removeLeft()
                else:
                    parent.removeRight()
            else:
                node.setRoot(None)
        elif children_count == 1:
            if not left.isEmpty():
                n = left
            else:
                n = right
            if parent is not None:
                if parent.getLeft() == node:
                    parent.setLeft(n)
                else:
                    parent.setRight(n)
            else:
                node = n
        else:
            # find its successor
            parent = node
            successor = left
            while not successor.getRight().isEmpty():
                parent = successor
                successor = successor.getRight()
            # replace node data by its successor data
            node.setRoot(successor.getRoot())
            # fix successor's parent's child
            if parent.getLeft() == successor:
                parent._left = parent.getLeft().getLeft()
            else:
                parent._right = parent.getRight().getLeft()

        return value
def debug_remove():
    tree = BST()
    tree.add((50,50))
    tree.add((30,30))
    # tree.add(60)
    # tree.add(9)
    # tree.add(34)
    # tree.add(58)
    # tree.add(80)
    # tree.add(18)
    # tree.add(32)
    # tree.add(47)
    # tree.add(53)
    # tree.add(55)
    print "\nTree:\n" + str(tree)

    data = (30,30)
    res = tree.remove(data)
    print "Remove:", data, " -> ", res
    print "\nTree:\n" + str(tree)
  
def main():
    tree = BST()
    print "Adding D B A C F E G"
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")
    
    print tree.find("A")
    print tree.find("Z")

    print "\nString:\n" + str(tree)

    print "Iterator (inorder traversal): "
    iterator = iter(tree)
    while True:
        try:
            print iterator.next(),
        except Exception, e:
            print e
            break
    
    # Use a for loop instead
    print "\nfor loop (inorder traversal): "
    for item in tree:
        print item,

if __name__ == "__main__":
  # main()
    debug_remove()




