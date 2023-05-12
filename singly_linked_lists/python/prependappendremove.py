class Node:
    def __init__(self, value):
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

    def prependVal(self, value, before):
        newNode = Node(value)
        runner = self.head
        if self.head.value == before:
            newNode.next = self.head
            self.head = newNode
        else:
            while runner is not None:
                if runner == self.tail:
                    self.tail.next = newNode
                    self.tail = newNode
                    break
                elif runner.next.value == before:
                    tempNode = runner.next
                    runner.next = newNode
                    newNode.next = tempNode
                    break
                runner = runner.next
        return self.display()

    def appendVal(self, value, after):
        newNode = Node(value)
        runner = self.head
        while runner is not None:
            if runner.value == after:
                tempNode = runner.next
                runner.next = newNode
                newNode.next = tempNode
                break
            elif runner == self.tail:
                self.tail.next = newNode
                self.tail = newNode
                break
            runner = runner.next
        return self.display()

    def removeVal(self, value):
        runner = self.head
        if self.head.value == value:
            tempNode = self.head
            self.head = tempNode.next
        else:
            while runner is not None:
                if runner.next.value == value:
                    tempNode = runner.next
                    runner.next = tempNode.next
                    break
                runner = runner.next
        return self.display()

SLL1 = SLL()
SLL1.addFront(5)
SLL1.addFront(4)
SLL1.addFront(3)
SLL1.addFront(2)
SLL1.addFront(1)
SLL1.addFront(0)
print(SLL1.display())
print(SLL1.prependVal(10,0))
print(SLL1.appendVal(10,7))
print(SLL1.removeVal(10))
print(SLL1.removeVal(10))