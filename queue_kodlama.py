"""
Queue()

enqueue(element)
dequeue()
size()
isEmpty()
"""

class Queue():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []
    
    def enqueue(self,element):
        self.elements.insert(0,element)

    def dequeue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)
    
myQueue = Queue()
myQueue.isEmpty()
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.dequeue()
myQueue.size()
myQueue.dequeue()
myQueue.dequeue()
myQueue.isEmpty()



