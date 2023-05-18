import math

def removeNegatives(arr):
    arr[:] = [x for x in arr if x > 0]
    return arr

# print(removeNegatives([1,-2,3,-4,5,-6]))


def secondToLast(arr):
    if len(arr) < 2:
        return None
    else:
        return arr[-2]

def secondToLast2(arr):
    length = 0
    for i in arr:
        length += 1
    if length < 2:
        return None
    else:
        index = 0
        while index != (length-2):
            index += 1
        return arr[index]

# print(secondToLast([42,True,4,"Kate",7]))
# print(secondToLast2([42,True,4,"Kate",7]))


def secondLargest(arr):
    if len(arr) <= 2:
        return None
    else:
        s = sorted(set(arr))
        return s[-2]

def secondLargest2(arr):
    if len(arr) <= 2:
        return None
    else:
        first = 0
        second = 0
        for i in arr:
            if i > first:
                first = i
        for i in arr:
            if i > second and i != first:
                second = i
        return second

# print(secondLargest([42,1,4,math.pi,7]))
# print(secondLargest2([42,1,4,math.pi,7]))


def nthToLast(list, n):
    if n > len(list):
        print("None")
        return None
    if n == 0:
        n = 1
    print(list[len(list)-n])

# nthToLast([5,2,3,6,4,9,7],7)


def nthLargest(list, n):
    x = max(list)
    y = 0
    if n > len(list):
        return None
    while n-1 != 0:
        for i in range(len(list)):
            if list[i] > y and list[i] < x:
                y = list[i]
        n -= 1
        x = y
        y = 0
    print(x)

# nthLargest([5,2,3,6,8,4,9,7],4)


def skylineHeights(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] > 0 and answer ==[]:
            answer.append(arr[i])
        elif answer != []:
            if arr[i] > answer[-1]:
                answer.append(arr[i])
    print(answer)


skylineHeights([0,4])
skylineHeights([-1,7,3])
skylineHeights([-1,1,1,7,3])