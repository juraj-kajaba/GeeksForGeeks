def selectionSort(arrToSort):
    """Implementation of selection sort algorithm.
    We divide input array into two parts, sublist of items already sorted
    and the sublist of items remaining to be sorted. We will first find
    the smallest element in unsorted list and this item is placed at the end of
    sorted list.

    Args:
        arrToSort: Array to be sorted. Will remain unchanged

    Returns:
        Sorted array
    """

    sortedArray = []
    unsortedArray = arrToSort[:]

    # While unsortedArray is not empty do sorting
    while unsortedArray:
        currentMin = None
        currentMinIdx = -1

        # Find the min value in the unsorted array
        for i in range(0, len(unsortedArray)):
            if currentMin == None or currentMin > unsortedArray[i]:
                currentMin = unsortedArray[i]
                currentMinIdx = i

        sortedArray.append(unsortedArray.pop(currentMinIdx))

    return sortedArray


# Tests        
a = [3, 2, 1,2,1,44,7,88,5,6,99]

print(a)
print(selectionSort(a))
