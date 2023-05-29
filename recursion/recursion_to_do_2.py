def rFib(n):
    n = int(n)
    if n == 0 or n == 1:
        return n
    else:
        return rFib(n-1) + rFib(n-2)

# print(rFib(8.7))

def rTrib(n):
    n = int(n)
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return rTrib(n-1) + rTrib(n-2) + rTrib(n-3)

# print(rTrib(6))

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

# print(ackermann(4,1))