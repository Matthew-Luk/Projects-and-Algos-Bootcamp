def as_coins(n):
    coins = {
        "Quarters": 0.25,
        "Dimes": 0.10,
        "Nickels": 0.05,
        "Pennies": 0.01
    }
    result = {
        "Quarters": 0,
        "Dimes": 0,
        "Nickels": 0,
        "Pennies": 0
    }
    for i in coins.keys():
        while coins[i] <= n:
            result[i] += 1
            n -= coins[i]
    return result

print(as_coins(1.57))


def maxMinAverage(arr):
    result = {
        "Max": 0,
        "Min": arr[0],
        "Average": 0
    }
    count = 0
    for i in range(len(arr)):
        result["Average"] += arr[i]
        count += 1
        if arr[i] < result["Min"]:
            result["Min"] = arr[i]
        if arr[i] > result["Max"]:
            result["Max"] = arr[i]
    result["Average"] = result["Average"] / count
    print(result)

maxMinAverage([1,2,3,4,5,6,7,8,9,10])