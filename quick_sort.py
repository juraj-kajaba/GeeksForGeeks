def sortPivot(arrToSort, start, end):
    """Reorder the array where pivot is the last element. 
    All elements higher as pivot will be on right side while the lower elements will be on the left side.
    Pivot element will be on the right place

    Args:
        arrToSort: Array to be sorted
        start: start index
        end: end index

    Returns:
        Index of pivot
    """

    pivot = arrToSort[end]
    lastSmallerThenPivot = start - 1

    # Track all elements in the array and for those lower than pivot 
    # swap currentIndex and lastSmallerThenPivot and move lastSmallerThenPivot by one afterwards
    for currentIndex in range(start,end):
        if (arrToSort[currentIndex] <= pivot ):
            lastSmallerThenPivot += 1
            arrToSort[lastSmallerThenPivot], arrToSort[currentIndex] = arrToSort[currentIndex], arrToSort[lastSmallerThenPivot]

    # Place pivot to the right place
    arrToSort[lastSmallerThenPivot + 1], arrToSort[end] = arrToSort[end], arrToSort[lastSmallerThenPivot + 1]

    return lastSmallerThenPivot + 1
    

def quickSort(arrToSort, start, end):
    """Implementation of quick sort algorithm.
    At first it select the pivot (last element of the array) and sort the array lower from pivot will
    be on the left side and higher values will be on the right side.
    
    Args:
        arrToSort: Array to be sorted
        start: start index
        end: end index

    Returns:
        None
    """

    if (end > start):
        # Reorder all elements around the pivot. Greater values will bo after pivot while lower values will be before it.
        # Pivot is already on the right position, return index of the pivot
        pivotIndex = sortPivot(arrToSort, start, end)

        # Sort subarray before pivot
        quickSort(arrToSort, start, pivotIndex-1)

        # Sort subarray after pivot
        quickSort(arrToSort, pivotIndex + 1, end)



# Tests
a = [10,80,90,40,30,20,70,45,78,54,78,65,98,98,1,2,1,4,8,7,4]
#print(a)
#quickSort(a, 0, len(a) - 1)
#print(a)

#a = [98, 98, 70, 80, 90, 98, 78, 98, 65, 78, 98]
print(a)

#sortPivot(a, 0, len(a)-1)
quickSort(a, 0, len(a)-1)
print(a)