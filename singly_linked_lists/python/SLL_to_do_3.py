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

    def secondLargestValue(self):
        runner = self.head
        first = 0
        second = 0
        location = 0
        index = 0
        while runner != None:
            if runner.value > first:
                first = runner.value
                location = index
            index += 1
            runner = runner.next
        runner = self.head
        if first == self.head.value:
            runner = self.head.next
        index = 0
        while runner != None:
            if runner.value > second:
                if runner.value <= first and index != location:
                    second = runner.value
            index += 1
            runner = runner.next
        print(f"First largest value: {first} Second largest value: {second}")

    def zip(self, SLL2):
        runner = self.head
        runner2 = SLL2.head
        newSLL = SLL()
        while runner != None and runner2 != None:
            newSLL.addBack(runner.value)
            newSLL.addBack(runner2.value)
            runner = runner.next
            runner2 = runner2.next
        if runner != None:
            while runner != None:
                newSLL.addBack(runner.value)
                runner = runner.next
        elif runner2 != None:
            while runner2 != None:
                newSLL.addBack(runner2.value)
                runner2 = runner2.next
        return newSLL.display()

    def removeDuplicates(self):
        duplicates = {self.head.value}
        slow = self.head
        fast = self.head.next
        while fast != None:
            if fast.value not in duplicates:
                duplicates.add(fast.value)
                slow = slow.next
            else:
                slow.next = fast.next
            fast = fast.next
        return self.display()

    def removeDuplicatesWithoutBuffer(self):
        duplicates = {self.tail.value}
        runner = self.head
        while runner.next != None:
            if runner.value not in duplicates:
                duplicates.add(runner.value)
                runner = runner.next
            else:
                runner.value = runner.next.value
                runner.next = runner.next.next
        return self.display()


SLL1 = SLL()
SLL2 = SLL()
SLL1.addFront(5)
SLL1.addFront(5)
SLL1.addFront(4)
SLL1.addFront(4)
SLL1.addFront(3)
SLL1.addFront(3)
SLL1.addFront(2)
SLL1.addFront(2)
SLL1.addFront(1)
SLL1.addFront(1)
SLL2.addFront(10)
SLL2.addFront(9)
SLL2.addFront(8)
SLL2.addFront(7)
SLL2.addFront(6)
# SLL1.display()
# SLL2.display()
SLL1.zip(SLL2)
# SLL1.secondLargestValue()
# SLL1.removeDuplicates()
# SLL1.removeDuplicatesWithoutBuffer()