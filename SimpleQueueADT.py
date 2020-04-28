# Angel De Pena
# methods of SimpleQueue = { enqueue(x), dequeue(), front(), length() }

# SimpleQueue.py

class SimpleQueue(object):

    def __init__(self):

        """ post: creates an empty FIFO queue """
        
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, x):

        """ post: adds x at back of queue """
        
        if self.size == 0:
            self.head = ListNode(x)
            self.tail = self.head
            self.size += 1
            
        else:
            self.tail.link = ListNode(x)
            self.size += 1

    def dequeue(self):

        """ pre: self.size > 0
            post: removes and returns the front item """
        
        if self.size == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return node.item

        elif self.size > 0:
            node = self.head
            self.head = node.link
            self.size -= 1
            return node.item
        
        else:
            return None

    def front(self):

        """ pre: self.size > 0
            post: returns first item in queue """
        
        if self.size > 0:
            return self.head.item
        
        else:
            return None

    def length(self):

        """ post: returns number of items in queue """

        return self.size

class ListNode(object):
    
    def __init__(self, item = None, link = None):
        
        '''post: creates a ListNode with the specified data value and link'''
        
        self.item = item
        self.link = link
