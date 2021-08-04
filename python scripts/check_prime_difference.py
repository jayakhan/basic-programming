''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

def isPrime(num):
    if num == 2: return True
    for count in range(2, num-1):
        if num % count == 0: return False
    return True

def fetchResult(F,S):
    if F == 0 and S == 0: return -1
    if F != 0 and S != 0: return S - F
    return 0

def result(L, R):
    if L == R:
        if isPrime(L) == True: return 0
        return -1
    firstPrime, secondPrime = 0, 0
    for i in range(L, R+1):
        if isPrime(i) == True:
            firstPrime = i
            break
        next
    if firstPrime != 0:
            for j in reversed(range(L, R+1)):
                if isPrime(j) == True:
                    secondPrime = j
                    break
                next
    return fetchResult(firstPrime, secondPrime)

def main():
    L = 5
    R = 6
    if sys.getsizeof(L) >= 2 and sys.getsizeof(L) <= sys.getsizeof(R) and sys.getsizeof(R) <= 1000000:
        print(result(L, R))

main()