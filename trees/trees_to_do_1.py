class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def add(rootNode, value):
    if rootNode.value == None:
        rootNode.value = value
    else:
        newNode = BSTNode(value)
        if value < rootNode.value:
            if rootNode.left == None:
                rootNode.left = newNode
            else:
                add(rootNode.left, value)
        elif value >= rootNode.value:
            if rootNode.right == None:
                rootNode.right = newNode
            else:
                add(rootNode.right, value)

def contains(rootNode, searchValue):
    if rootNode == None:
        return False
    if rootNode.value == searchValue:
        return True
    if searchValue < rootNode.value:
        return contains(rootNode.left, searchValue)
    return contains(rootNode.right, searchValue)

def min(rootNode):
    while rootNode.left != None:
        rootNode = rootNode.left
    return rootNode.value

def max(rootNode):
    while rootNode.right != None:
        rootNode = rootNode.right
    return rootNode.value

def size(rootNode):
    if rootNode == None:
        return 0
    return 1 + size(rootNode.left) + size(rootNode.right)

def isEmpty(rootNode):
    if rootNode.value == None:
        return True
    return False

def preOrderTraversal(rootNode):
    if rootNode == None:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

def inOrderTraversal(rootNode):
    if rootNode == None:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.value)
    inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if rootNode == None:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.value)

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        printTree(node.right, level + 1)

newBST = BSTNode()
add(newBST, 5)
add(newBST, 10)
add(newBST, 9)
add(newBST, 7)
add(newBST, 8)
add(newBST, 6)
add(newBST, 4)
add(newBST, 3)
add(newBST, 2)
add(newBST, 1)
add(newBST, 0)
# printTree(newBST)
# print(contains(newBST, 4))
# print(min(newBST))
# print(max(newBST))
# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# print(size(newBST))
# print(isEmpty(newBST))