import math
def binary_search(list, targetVal):
    min = 0
    max = len(list) - 1
    i = 0
    while(max >= min):
        guess = int((max+min)/2)
        print("Guess is: ", str(guess))
        i += 1
        if(list[guess] == targetVal):
            print("Target value is found in guess: " , str(i))
            return guess
        elif(list[guess] < targetVal):
            min = guess + 1
        else:
            max = guess - 1
    return -1

list = [2,4,5,6,7,8,12,15,19,23,25,27,29,34,37,49,51,52,53,56,59,65,66,67,89]

print("Found at: ", binary_search(list, 29))

        
