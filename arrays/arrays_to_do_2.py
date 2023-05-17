# While loop
def reverse1(arr):
    i = 0
    while i < (len(arr)//2):
        temp = arr[i]
        arr[i] = arr[-1-i]
        arr[-1-i] = temp
        i += 1
    print(arr)

# For loop
def reverse2(arr):
    for i in range(int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[-1-i]
        arr[-1-i] = temp
    print(arr)

list = [12,239,59,10,28,99]
print(list)
reverse1(list)
reverse2(list)


def rotateArr(arr, shiftBy):
    if shiftBy > len(arr):
        shiftBy = shiftBy % len(arr)
        print(shiftBy)
    elif shiftBy == len(arr):
        print(arr)
    else:
        print(arr[-shiftBy:] + arr[:-shiftBy])

def rotateArr(arr, shiftBy):
    shiftBy = shiftBy % len(arr)
    if shiftBy == 0:
        print(arr)
    else:
        print(arr[-shiftBy:] + arr[:-shiftBy])

rotateArr([1,2,3],-2)


def filterRange(arr, min, max):
    answer = []
    for i in range(len(arr)):
        if arr[i] > min and arr[i] < max:
            answer.append(arr[i])
    print(answer)

list = [6,4,7,1,8,2,5,3,9,10]
filterRange(list, 4, 9)


def concat1(arr1, arr2):
    print(arr1 + arr2)

def concat2(arr1, arr2):
    result = []
    for i in arr1:
        result.append(i)
    for i in arr2:
        result.append(i)
    print(result)

list1 = [0,1,2,3]
list2 = [4,5,6,7]
concat1(list1, list2)
concat2(list1, list2)