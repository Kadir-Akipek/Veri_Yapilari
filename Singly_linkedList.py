"""
Singly linked List

Listelerden farkı, bir şeyi kolaylıkla ekleyebiliriz veya
bir şeyi okurken zorlanabiliriz(istisnai durumlar hariç)
"""

class Node():
    def __init__(self,value):
        self.value = value
        self.nextNode = None

firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
firstNode.nextNode.value #secondNode value
firstNode.nextNode.nextNode.value #thirdNode value