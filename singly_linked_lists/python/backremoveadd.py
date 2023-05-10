class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

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

    def display(self):
        runner = self.head
        result = ""
        while runner != None:
            if runner.next != None:
                result = result + str(runner.value) + ", "
            else:
                result = result + str(runner.value)
            runner = runner.next
        return result

    def back(self):
        runner = self.head
        while runner != None:
            if runner.next == None:
                return runner.value
            runner = runner.next

    def removeBack(self):
        runner = self.head
        while runner != None:
            if runner.next.next == None:
                runner.next = None
                self.tail = runner
            runner = runner.next
        return self.display()

    def addBack(self, value):
        newNode = Node(value)
        # runner = self.head
        # while runner != None:
        #     if runner.next == None:
        #         runner.next = newNode
        #         return runner.value
        #     runner = runner.next
        newNode.next = None
        self.tail.next = newNode
        self.tail = newNode

SLL1 = SLL()
SLL1.addFront(5)
SLL1.addFront(4)
SLL1.addFront(3)
SLL1.addFront(2)
SLL1.addFront(1)
SLL1.addFront(0)
SLL1.addBack(6)
SLL1.addBack(8)
SLL1.addBack(7)
SLL1.removeBack()
print(SLL1.display())