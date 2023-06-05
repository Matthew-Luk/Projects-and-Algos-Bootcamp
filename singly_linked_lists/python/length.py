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

    def length(self):
        runner = self.head
        count = 0
        while runner != None:
            print(runner.value)
            count += 1
            runner = runner.next
        return count

SLL1 = SLL()
SLL1.addFront(1)
SLL1.addFront(2)
SLL1.addFront(3)
SLL1.addFront(4)
SLL1.addFront(5)
print(SLL1.length())
print([node.value for node in SLL1])