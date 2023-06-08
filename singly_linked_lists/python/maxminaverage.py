class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        runner = self.head
        count = 0
        while runner != None:
            print(runner.value)
            count += 1
            runner = runner.next
        return count

    def addFront(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def max(self):
        runner = self.head
        max = 0
        while runner != None:
            if max < runner.value:
                max = runner.value
            runner = runner.next
        return max

    def min(self):
        runner = self.head
        min = self.head.value
        while runner != None:
            if min > runner.value:
                min = runner.value
            runner = runner.next
        return min

    def average(self):
        if self.head is None:
            return None
        else:
            runner = self.head
            sum = 0
            while runner != None:
                sum += runner.value
                runner = runner.next
            return (sum/self.length())

SLL1 = SLL()
SLL1.addFront(76)
SLL1.addFront(2)
SLL1.addFront(11.41)
print(SLL1.max())
print(SLL1.min())
print(SLL1.average())