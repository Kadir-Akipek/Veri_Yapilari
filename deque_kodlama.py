"""
Deque()

addRight()
addLeft()
removeRight()
removeLeft()
isEmpty()
size()
"""

class Deque():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def addRight(self,element):
        return self.elements.append(element)

    def addLeft(self,element):
        return self.elements.insert(0,element)
    
    def removeRight(self):
        return self.elements.pop()
    
    def removeLeft(self):
        return self.elements.pop(0)
    
    def size(self):
        return len(self.elements)
    
myDeque = Deque()
myDeque.addRight(10)
myDeque.addRight(20)
myDeque.addLeft(30)
myDeque.addLeft(40)
myDeque.addRight(50)
myDeque.size()
myDeque.removeLeft()
myDeque.removeLeft()
myDeque.removeRight()
myDeque.size()