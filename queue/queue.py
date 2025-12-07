class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head == None:
            return None
        return self.head.data
    

    def peekBack(self):
        if self.tail == None:
            return None
        return self.tail.data
    
    def enqueue(self, data):
        new_data = Node(data)
        if self.tail == None:
            self.head = new_data
            self.tail = new_data
        else:
            self.tail.next = new_data
            self.tail = new_data
    
    def dequeue(self):
        if self.head == None:
            return None
        temp = self.head
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return temp.data



