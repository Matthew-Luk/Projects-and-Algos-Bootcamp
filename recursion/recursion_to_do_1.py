def rSigma(n):
    n = int(n)
    if n <= 0:
        return 0
    else:
        return n + rSigma(n-1)

print(rSigma(2.5))

def rFactorial(n):
    n = int(n)
    if n <= 0:
        return 1
    else:
        return n * rFactorial(n-1)

print(rFactorial(6.5))