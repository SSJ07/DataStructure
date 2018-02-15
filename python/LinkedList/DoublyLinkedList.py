'''
@author: shrikant_jagtap
'''

class Node:
    '''
        Node contains actual value.
        And pointers which point previous node and next in list.
    '''
    def __init__(self, value):
        ''' constructor to initialize values'''
        self.value = value
        self.next = None
        self.prev = None
        
    def __repr__(self):
        ''' class representation as string '''
        return str(self.value)
    
    

class DoublyLinkedList:
    '''
        Abstract class provides functions to operates list
    '''
    
    def __init__(self):
        ''' constructor to initialize intial root value'''
        self.root = None
    
    def getLastNode(self):
        ''' get last node in LL '''
        node = self.root
        while node.next!=None:
            node = node.next
        return node
    
    def addItem(self, value):
        ''' add/append item to LL''' 
        if self.root == None:
            self.root = Node(value)
        else:
            node = self.getLastNode()
            tmp = Node(value)
            tmp.next = None
            tmp.prev = node
            node.next = tmp
            
    def insertItem(self, index, value):
        ''' insert item at given position in LL'''
        tmp = Node(value)
        if index == 1:
            ''' insert as root'''
            tmp.prev = None
            tmp.next = self.root
            self.root.prev = tmp
            self.root = tmp 
        else:
            node = self.root 
            while index > 1:
                node = node.next
                index-=1
            tmp.prev = node.prev
            node.prev.next = tmp
            tmp.next = node   
            node.prev = tmp
            
    def removeItem(self, value):
        ''' remove an item from LL'''
        if self.root.value == value:
            ''' if value found in first node/root'''
            self.root = self.root.next
            self.root.prev.next = None
            self.root.prev = None
        else:
            node = self.root
            while node!=None:
                if node.value == value:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node.next = None
                    node.prev = None
                    break
                node = node.next
            
    def printList(self):
        ''' print LL'''
        node = self.root
        while node!=None:
            print(node.value, end=" ")
            node = node.next
        print()
        
    def printReverse(self):
        node = self.getLastNode()
        while node!=None:
            print(node.value, end=" ")
            node = node.prev
        print()

if __name__ == '__main__':
    doublyLL = DoublyLinkedList()
    doublyLL.addItem(10)
    doublyLL.addItem(20)
    doublyLL.addItem(30)
    doublyLL.addItem(40)
    doublyLL.printList()
    print("**********Reverse order double linked list*************")
    doublyLL.printReverse()
    doublyLL.insertItem(2, 15)
    doublyLL.insertItem(1, 5)
    print("************after inserting item double linked list is **************")
    doublyLL.printList()
    
    doublyLL.removeItem(5)
    print("********** after removing item 5 from list ************")
    doublyLL.printList()
    
    doublyLL.removeItem(20)
    print("********** after removing item 20 from list ************")
    doublyLL.printList()
    
    print("Last item in DLL is : {}".format(doublyLL.getLastNode()))
