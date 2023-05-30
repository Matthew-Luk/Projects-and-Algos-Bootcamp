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

    def removeFront(self):
        if self.head is None:
            return None
        else:
            removeNode = self.head
            self.head = removeNode.next
            removeNode.next = None

    def front(self):
        if self.head is None:
            return None
        else:
            return self.head.value

    def contains(self, value):
        runner = self.head
        while runner.next != None:
            runner = runner.next
            if runner.value == value:
                return True
        return False

    def length(self):
        runner = self.head
        count = 0
        while runner != None:
            print(runner.value)
            count += 1
            runner = runner.next
        return count

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
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

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
SLL1.addFront(18)
SLL1.addFront(5)
SLL1.addFront(73)
SLL1.removeFront()
SLL1.removeFront()
print(SLL1.front())
print(SLL1.removeFront())
print(SLL1.front())
print(SLL1.average())
# print([node.value for node in SLL1])