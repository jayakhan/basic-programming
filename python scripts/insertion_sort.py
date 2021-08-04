def insert(list, rightIndex, value):
    while rightIndex >=0 and list[rightIndex] > value:
        list[rightIndex + 1] = list[rightIndex]
        rightIndex -= 1
    list[rightIndex + 1] = value
        
def insertion_sort(list):
    for i in range(1, len(list)):
        insert(list, i-1, list[i])

list = [22, 11, 99, 88, 9, 7, 42]
insertion_sort(list)
print("Sorted list", str(list))

"""
0,11 > 22,22,99,88,9,7,42 > 11,22,99,88,9,7,42
1,99 > 11,22,99,88,9,7,42
2,88 > 11,22,99,99,9,7,42 > 11,22,88,99,9,7,42
3,9 > 11,22,88,99,99,7,42 > 11,22,88,88,99,7,42 > 11,22,22,88,99,7,42 > 11,11,22,88,99,7,42 > 9,11,22,88,99,7,42
4,7 > 9,11,22,88,99,99,42 > 9,11,22,88,88,99,42 > 9,11,22,22,88,99,42 > 9,11,11,22,88,99,42 > 9,9,11,22,88,99,42 > 7,9,11,22,88,99,42
5,42 > 7,9,11,22,88,99,99 > 7,9,11,22,88,88,99 > 7,9,11,22,42,88,99
"""