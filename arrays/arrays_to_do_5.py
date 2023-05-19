def average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)

# print(average([1,2,3,4,10]))

def balancePoint(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i:]):
            return True
    return False

# print(balancePoint([1,2,3,4,10]))

def balanceIndex(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

print(balanceIndex([-2,5,7,0,3]))
print(balanceIndex([9,9]))