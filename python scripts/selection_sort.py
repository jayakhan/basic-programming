def swap(list, firstIndex, secondIndex):
    list[firstIndex], list[secondIndex] = list[secondIndex], list[firstIndex]

def index_of_min_val(list, startIndex):
    minVal = list[startIndex]
    minIndex = startIndex
    for j in range(startIndex+1, len(list)):
        if(list[j] < minVal):
            minIndex = j
    return minIndex

def selection_sort(list):
    for i in range(len(list)):
        foundIndex = index_of_min_val(list, i)
        swap(list,i,foundIndex)

list = [10,2,11,23,22,22]
selection_sort(list)

print("Sorted list", str(list))