def insertionSort(arrToSort):
    """Implementation of insertion sort algorithm.
    We go through the array from the begin to the end. Each element will be at first
    popped from the unsorted array and then will be finded proper position in sorted array

    Args:
        arrToSort: Array to be sorted. Will remain unchanged

    Returns:
        Sorted array
    """

    sortedArray = []
    unsortedArray = arrToSort[:]

    # While unsortedArray is not empty do sorting
    while unsortedArray:
        item = unsortedArray.pop(0)

        isFound = False
        # Find the proper position in sorted array and insert item into it
        for i in range(0, len(sortedArray)):
            if item < sortedArray[i]:
                sortedArray.insert(i, item)
                isFound = True
                break
        
        # Append if there is no larger value in sorted array 
        if not isFound:
            sortedArray.append(item)

    return sortedArray


# Tests        
a = [3, 2, 1,2,1,44,7,88,5,6,99]

print(a)
print(insertionSort(a))
