"""
Doubly linked list

Singly linked list' den farklı olarak listenin 
başında ve sonunda Header ve Trailer adlı 2 adet 
Node bulunur
Genellikle Doubly linked list kullanırız
"""

class DoublyNode():
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.previousNode = None

x = DoublyNode(5)
y = DoublyNode(10)
z = DoublyNode(15)

x.nextNode = y
y.previousNode = x
y.nextNode = z
z.previousNode = y 
x.nextNode.nextNode.value #z value
z.previousNode.previousNode.value #x value