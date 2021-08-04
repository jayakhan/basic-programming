def palindrome(str):
    if(len(str) <= 1):
        return 'yes'
    elif(str[0] != str[-1]):
        return 'no'
    return palindrome(str[1:-1])

test_string = 'xyx'
result = palindrome(test_string)
print("Is it palindrome?:  ", str(result))