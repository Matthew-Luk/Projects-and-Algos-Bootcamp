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

def height(rootNode):
    if rootNode == None:
        return -1
    else:
        # we are adding 1 and then going with left or right depending on which one is taller
        return 1 + max(height(rootNode.left), height(rootNode.right))

def isBalanced(rootNode):
    if rootNode == None:
        return True
    # getting the value or left height
    lh = height(rootNode.left)
    # getting the value of right height
    rh = height(rootNode.right)
    # checking to make sure left and right height are even, then traversing left and right node and doing the same
    if abs(lh - rh) <= 1 and isBalanced(rootNode.left) and isBalanced(rootNode.right):
        return True
    return False

def arr2Bst(arr):
    if arr == []:
        return
    mid = len(arr) // 2
    root = BSTNode(arr[mid])
    root.left = arr2Bst(arr[:mid])
    root.right = arr2Bst(arr[mid+1:])
    return root

def contains(rootNode, searchValue):
    if not rootNode:
        return False
    if rootNode.value == searchValue:
        return True
    if searchValue < rootNode.value:
        return contains(rootNode.left, searchValue)
    return contains(rootNode.right, searchValue)

def inOrderTraversal(rootNode):
    if rootNode == None:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.value)
    inOrderTraversal(rootNode.right)

def preOrderTraversal(rootNode):
    if rootNode == None:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if rootNode == None:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.value)

def CCA(rootNode, value1, value2):
    # this statement is just to make sure value 1 is the lower number and value 2 is the higher number
    if value2 < value1:
        temp = value1
        value1 = value2
        value2 = temp
    # we return the current node if the value1 is on the left and value2 is on the right
    if contains(rootNode.left, value1) and contains(rootNode.right, value2):
        return rootNode.value
    # if both values are less than root value we need to go to the left node and check
    if value1 < rootNode.value and value2 < rootNode.value:
        return CCA(rootNode.left, value1, value2)
    # if both values are higher than root value we need to go to the right node and check
    return CCA(rootNode.right, value1, value2)

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        printTree(node.right, level + 1)

newBST = BSTNode()
add(newBST, 6)
add(newBST, 5)
add(newBST, 2)
add(newBST, 3)
add(newBST, 4)
add(newBST, 1)
add(newBST, 7)

# print(height(newBST))
printTree(newBST)
# print(isBalanced(newBST))



# print(contains(newBST, 8))
# list = [1,2,3,4,5,6,7,8,9,10]
# preOrderTraversal(arr2Bst(list))
# inOrderTraversal(newBST)
# inOrderTraversal(arr2Bst(list))
# postOrderTraversal(arr2Bst(list))
# print(isBalanced(arr2Bst(list)))

# CCA testing
# newBST = BSTNode()
# add(newBST, 6)
# add(newBST, 3)
# add(newBST, 9)
# add(newBST, 2)
# add(newBST, 5)
# add(newBST, 8)
# add(newBST, 10)
# add(newBST, 1)
# add(newBST, 4)
# add(newBST, 7)
# print(CCA(newBST, 1, 4))