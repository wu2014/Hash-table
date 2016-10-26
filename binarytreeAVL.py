from binarytree import *

class BinaryTreeAVL(BinaryTree):
    def __init__(self, item, balance = 'EQ'):
        BinaryTree.__init__(self, item)
        self._balance = balance

    def getBalance(self):
        return self._balance

    def setBalance(self, newBalance):
        self._balance = newBalance

    def __str__(self):
        """Returns a string representation of the tree
        rotated 90 degrees to the left."""
        def strHelper(tree, level):
            result = ""
            if not tree.isEmpty():
                result += strHelper(tree.getRight(), level + 1)
                result += "| " * level
                result += str(tree.getRoot())+ " : " + tree.getBalance() + "\n"
                result += strHelper(tree.getLeft(), level + 1)
            return result
        return strHelper(self, 0)
    
    