def merge(list, p, q, r):
    lowHalf = []
    highHalf = []
    k = p
"""Adding element from list to lowHalf and highHalf lists """
    for i in list[k:q+1]:
        lowHalf.append(i)
        k += 1

    for j in list[k:r+1]:
        highHalf.append(j) 

    k = p
    i, j = 0, 0

"""Comparing element between lowHalf and highHalf and adding it to main list"""
    while(i < len(lowHalf) and j < len(highHalf)):
        if lowHalf[i] < highHalf[j]:
            list[k] =  lowHalf[i]
            i += 1
        else:
            list[k] = highHalf[j]
            j += 1
        k += 1

"""Adding remaining elements, if left, from lowHalf and highHalf lists to main list"""
    while(i < len(lowHalf)):
        list[k] = lowHalf[i]
        i += 1
        k += 1
    
    while(j < len(highHalf)):
        list[k] = highHalf[j]
        j += 1
        k += 1

""" Dividing list into sublists"""
def merge_sort(list, startIndex, endIndex):
    if startIndex < endIndex:
        middleIndex = int((startIndex + endIndex)/2)
        merge_sort(list, startIndex, middleIndex)
        merge_sort(list, middleIndex + 1, endIndex)
        merge(list, startIndex, middleIndex, endIndex)

list = [14, 7, 3, 12 ,9, 11, -6, 2, 0]
merge_sort(list, 0, len(list))
print("Array after sorting: ", str(list))