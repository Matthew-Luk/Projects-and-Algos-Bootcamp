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

    def min(self):
        runner = self.head
        min = self.head.value
        while runner != None:
            if min > runner.value:
                min = runner.value
            runner = runner.next
        return min

    def minToFront(self):
        # Finding the min value
        runner = self.head
        min = self.head.value
        while runner != None:
            if min > runner.value:
                min = runner.value
            runner = runner.next

        # Removing the min value
        if self.head.value == min:
            return self.display()
        else:
            runner = self.head
            while runner is not None:
                if runner.next.value == min:
                    nextNode = runner.next
                    runner.next = nextNode.next
                    break
                runner = runner.next

        # Appending the min value to the front
        minNode = Node(min)
        minNode.next = self.head
        self.head = minNode
        return self.display()

    def maxToBack(self):
        # Find the max value
        runner = self.head
        max = self.head.value
        while runner is not None:
            if max < runner.value:
                max = runner.value
            runner = runner.next

        # Removing the max value
        if self.tail.value == max:
            return self.display()
        else:
            runner = self.head
            while runner is not None:
                if runner.next.value == max:
                    nextNode = runner.next
                    runner.next = nextNode.next
                    break
                runner = runner.next

        # Appending the max value to the back
        maxNode = Node(max)
        maxNode.next = None
        self.tail.next = maxNode
        self.tail = maxNode
        return self.display()



SLL1 = SLL()
SLL1.addFront(1)
SLL1.addFront(2)
SLL1.addFront(0)
SLL1.addFront(3)
SLL1.addFront(4)
SLL1.addFront(5)
print(SLL1.display())
print(SLL1.minToFront())
print(SLL1.minToFront())