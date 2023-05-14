class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def removeSelf(self):
        self.value = self.next.value
        self.next = self.next.next

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFront(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addBack(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def display(self):
        runner = self.head
        result = ""
        while runner != None:
            if runner.next != None:
                result = result + str(runner.value) + ", "
            else:
                result = result + str(runner.value)
            runner = runner.next
        print(result)

    def secondToLast(self):
        if self.head == self.tail:
            print(f"The list only has one node: {self.head.value}")
            return self
        runner = self.head
        while runner is not None:
            if runner.next == self.tail:
                runner.next = None
                self.tail = runner
            runner = runner.next
        return runner.value

    def copy(self):
        runner = self.head
        newSLL = SLL()
        while runner != None:
            newSLL.addBack(runner.value)
            runner = runner.next
        print(id(self), id(newSLL))
        return self.display(), newSLL.display()

    def filter(self, lowVal, highVal):
        runner = self.head
        newSLL = SLL()
        while runner != None:
            if runner.value >= lowVal and runner.value <= highVal:
                newSLL.addBack(runner.value)
            runner = runner.next
        return newSLL.display()

SLL1 = SLL()
SLL1.addFront(5)
SLL1.addFront(4)
SLL1.addFront(3)
SLL1.addFront(2)
SLL1.addFront(1)
SLL1.addFront(0)
# SLL1.display()
# SLL1.head.next.next.next.removeSelf()
# SLL1.copy()
SLL1.filter(2,4)
# SLL1.display()