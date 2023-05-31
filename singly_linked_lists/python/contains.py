class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def addFront(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def contains(self, value):
        runner = self.head
        while runner.next != None:
            runner = runner.next
            if runner.value == value:
                return True
        return False

SLL1 = SLL()
SLL1.addFront(18)
SLL1.addFront(5)
SLL1.addFront(73)
print(SLL1.contains(18))
print([node.value for node in SLL1])