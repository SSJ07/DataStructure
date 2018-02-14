'''
@author: shrikant
'''
import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    def _insert(self, value, currentNode):
        if value < currentNode.value:
            if currentNode.left == None:
                currentNode.left = Node(value)
            else:
                self._insert(value, currentNode.left)
        elif value > currentNode.value:
            if currentNode.right == None:
                currentNode.right = Node(value)
            else:
                self._insert(value, currentNode.right)
        else:
            print("value already exist in tree")
    def printBTree(self):
        if self.root != None:
            self._printTree(self.root)
    def _printTree(self, node):
        if node:
            self._printTree(node.left)
            print(node.value)
            self._printTree(node.right)
        
def createTree(tree, maxNum=10, maxRange=100):
    for i in range(maxNum):
        num = random.randint(i, maxRange)
        tree.insert(num)
            
bTree  = BinaryTree()
createTree(bTree)
bTree.printBTree()
