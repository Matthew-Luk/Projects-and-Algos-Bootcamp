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

    def addBack(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

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

    def splitOnVal(self, num):
        runner = self.head
        slow = runner
        fast = runner.next
        if self.head.value == num:
            return SLL(), self
        while fast.value != num:
            slow = slow.next
            fast = fast.next
        slow.next = None

        SLL1 = SLL()
        SLL1.head = self.head
        SLL1.tail = slow

        SLL2 = SLL()
        SLL2.head = fast
        SLL2.tail = self.tail
        return SLL1, SLL2

    def removeNegatives(self):
        runner = self.head
        while runner.next is not None:
            if runner.next == self.tail:
                break
            if self.head.value < 0:
                tempNode = self.head
                self.head = tempNode.next
            if runner.next.value < 0:
                tempNode = runner.next
                runner.next = tempNode.next
            runner = runner.next
        if self.tail.value < 0:
            runner = self.head
            while runner is not None:
                if runner.next == self.tail:
                    runner.next = None
                    self.tail = runner
                runner = runner.next
        return self.display()

        # sentinel = node = Node()
        # sentinel.next = self.head
        # while node.next != None:
        #     if node.next.value < 0:
        #         # implies next node's value is negative
        #         node.next = node.next.next
        #     node = node.next
        # self.head = sentinel.next
        # self.display()

    def concat(self, sll2):
        self.tail.next = sll2.head
        self.tail = sll2.tail
        sll2.head = self.head
        return self.display()

    def partition(self, value):
        runner = self.head
        lowSLL = SLL()
        highSLL = SLL()
        count = 0
        while runner != None:
            if runner.value < value:
                lowSLL.addBack(runner.value)
            elif runner.value > value:
                highSLL.addBack(runner.value)
            else:
                count += 1
            runner = runner.next
        if count == 0:
            return self.display()
        lowSLL.addBack(value)
        lowSLL.concat(highSLL)
        return lowSLL.display()

    # def reverse(self):
    #     prev = None
    #     runner = self.head
    #     while runner != None:
    #         # next is just a temp variable to hold next value (ie. next == 2)
    #         next = runner.next
    #         # next pointer is previous number (ie. 1 -> None)
    #         runner.next = prev
    #         # prev moves up (ie. prev == 1)
    #         prev = runner
    #         # runner moves up (ie. runner == 2)
    #         runner = next
    #     # set head to prev to be able to display entire list
    #     self.head = prev

    def removeNthFromEnd(self, n):
        runner = self.head
        length = 0
        while runner != None:
            length += 1
            runner = runner.next
        if length == n:
            self.head = self.head.next
        else:
            runner = self.head
            index = 0
            length = length - n
            print(length)
            while index < length - 1:
                index += 1
                runner = runner.next
            runner.next = runner.next.next


SLL1 = SLL()
SLL1.addFront(5)
SLL1.addFront(4)
SLL1.addFront(3)
SLL1.addFront(2)
SLL1.addFront(1)
SLL1.display()
# SLL1.removeNegatives()
# SLL1.partition(3)
SLL1.removeNthFromEnd(2)
SLL1.display()
# list1, list2 = SLL1.splitOnVal(5)
# list1.display()
# list2.display()