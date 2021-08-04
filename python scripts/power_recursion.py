def power(x,n):
    if(n == 0):
        return 1
    if(n < 0):
        return 1/power(x, -n)
    if(n%2 == 0):
        y = power(x, n/2)
        return y*y
    if(n%2 != 0):
        return x*power(x, n-1)

print(power(25,-1))