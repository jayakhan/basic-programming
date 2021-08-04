def recursion(n):
    if(n == 0):
        return 1
    return n * recursion(n-1)

print("Factorial of 5 is:  ", str(recursion(5)))