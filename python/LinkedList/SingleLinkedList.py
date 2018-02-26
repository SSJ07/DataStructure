'''
@author: shrikant
'''

class Node:
    ''' This is node store data and link of next node '''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
        
class SingleLinkedList:
    ''' Single linked list data structure '''
    def __init__(self):
        self.root = None
        
    def addNode(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value)
    def _add(self, value):
        node = self.getLastNode()
        node.next = Node(value)
        
    def getFirstNode(self):
        node = self.root
        return node
    
    def getLastNode(self):
        node = self.root
        while node.next!=None:
            node = node.next
        return node
    def get(self, index):
        node = self.root
        if self.size() < index:
            print("Index is not valid")
        else:
            while index > 1:
                node = node.next
                index-=1
            return node
        return None
    def size(self):
        node = self.root
        count = 0
        while node!=None:
            count+=1
            node = node.next
        return count
    def remove(self, value):
        node = self.root.next
        prev = self.root
        if node.value == value:
            self.root = node.next
            node.next = None
        else:
            while node!=None:
                if node.value == value:
                    prev.next = node.next
                    node.next = None
                node = node.next
                prev = prev.next
    def insertAt(self, index, value):
        size = self.size()
        if index > size:
            print(" index is not valid")
        else:
            node = self.root
            while index > 2:
                node = node.next
                index-=1
            tmp =  Node(value)
            tmp.next = node.next
            node.next = tmp
            
    def printLinkedList(self):
        node = self.root
        while node!=None:
            print(node.value, end=" ")
            node = node.next
        print()


if __name__ == '__main__':
    singleLL = SingleLinkedList()
    singleLL.addNode(10)
    singleLL.addNode(20)
    singleLL.addNode(30)
    singleLL.printLinkedList()
    singleLL.insertAt(2, 25)
    singleLL.insertAt(4, 27)
    singleLL.printLinkedList()
    print("First node is :{}".format(singleLL.getFirstNode()))
    print("Last node is :{}".format(singleLL.getLastNode()))
    print("node at index 3 is : {}".format(singleLL.get(3)))
    singleLL.remove(27)
    print("After deletion node 27")
    singleLL.printLinkedList()
