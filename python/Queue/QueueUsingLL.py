'''

@author: shrikant
'''


class Node:
    '''
        Node store actual value.
        And link of next node.
    '''
    def __init__(self, val):
        self.val  = val
        self.next = None

    def __repr__(self):
        return str(self.val)
    
class Queue:
    '''
        Queue class provides abstract data structure operations
    '''
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, val):
        node = Node(val)
        if self.rear == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        if self.front == None:
            return None
        else:
            node = self.front
            self.front = self.front.next
            node.next = None
            return node
        
    def getFront(self):
        if self.front==None:
            return None
        return self.front
    
    def getRear(self):
        if self.rear == None:
            return None
        return self.rear
    
if __name__ == '__main__':
    
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    
    print("front item is :{}".format(queue.getFront()))
    print("rear item is :{}".format(queue.getRear()))
    
    queue.dequeue()
    print("front item after deleting item :{}".format(queue.getFront()))
