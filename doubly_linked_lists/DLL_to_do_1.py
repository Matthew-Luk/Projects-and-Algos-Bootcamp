class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        newNode = Node(value)
        newNode.next = None
        newNode.prev = None
        self.head = newNode
        self.tail = newNode
        print("The DLL has been successfully created")

    def display(self):
        runner = self.head
        result = ""
        while runner != None:
            result = result + str(runner.value) + " -> "
            runner = runner.next
        print(result[:-4])

    def displayReverse(self):
        runner = self.tail
        result = ""
        while runner != None:
            result = result + str(runner.value) + " -> "
            runner = runner.prev
        print(result[:-2])

    def addBack(self, value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def addFront(self, value):
        newNode = Node(value)
        if self.head == None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def reverse(self):
        newDLL = DLL()
        runner = self.tail
        while runner != None:
            newNode = Node(runner.value)
            if newDLL.head is None:
                newNode.next = None
                newNode.prev = None
                newDLL.head = newNode
                newDLL.tail = newNode
            else:
                newNode.prev = newDLL.tail
                newDLL.tail.next = newNode
                newDLL.tail = newNode
            runner = runner.prev
        return newDLL.display()

    def reverse2(self):
        prev = None
        runner = self.head
        while runner != None:
            next = runner.next
            runner.next = prev
            prev = runner
            runner = next
        self.head = prev
        return self.display()

    def kthLastNode(self, location):
        runner = self.tail
        index = 1
        while index < location:
            if runner == self.head:
                return "Location is out of list range"
            index += 1
            runner = runner.prev
        return runner.value

    def isPalindrome(self):
        runner1 = self.head
        runner2 = self.tail
        while runner1 != runner2:
            if runner1.value == runner2.value:
                runner1 = runner1.next
                runner2 = runner2.prev
            else:
                return False
        return True

    def shift(self, shiftBy):
        shiftedDLL = DLL()
        index = 0
        if shiftBy == 0:
            self.display()
        elif shiftBy > 0:
            runner = self.tail
            while index < shiftBy:
                shiftedDLL.addFront(runner.value)
                index += 1
                runner = runner.prev
            self.tail = runner
            runner.next.prev = None
            runner.next = None
            shiftedDLL.tail.next = self.head
            self.head.prev = shiftedDLL
            self.head = shiftedDLL.head
            self.display()
        elif shiftBy < 0:
            shiftBy = abs(shiftBy)
            runner = self.head
            while index < shiftBy +1:
                shiftedDLL.addBack(runner.value)
                index += 1
                runner = runner.next
            self.head = runner
            self.tail.next = shiftedDLL.head
            shiftedDLL.head.prev = self.tail
            self.tail = shiftedDLL.tail
            self.display()

DLL1 = DLL()
DLL1.createDLL(1)
DLL1.addBack(2)
DLL1.addBack(3)
DLL1.addBack(4)
DLL1.addBack(5)
DLL1.addBack(6)
# DLL1.addBack(6)
# DLL1.addBack(5)
# DLL1.addBack(4)
# DLL1.addBack(3)
# DLL1.addBack(2)
# DLL1.addBack(1)
# print(DLL1.isPalindrome())
DLL1.reverse()
DLL1.reverse2()
# DLL1.shift(3)
# DLL1.shift(-2)
# print(DLL1.kthLastNode(2))
DLL1.display()