def partition(list, p, q):
    

def quick_sort(list, startIndex, endIndex):
    if startIndex < endIndex:
        pivot = partition(list, startIndex, endIndex)
        quick_sort(list, startIndex, pivot-1)
        quick_sort(list, pivot+1, endIndex)

list = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
quick_sort(list, 0, len(list))
print("Array after sorting: " , str(list))