def bubbleSort(arrToSort):
    """Implementation of bubble sort algorithm.
    It walks through the array and compares two neighbor elements. If left element is greater then right one
    then elements will be swapped. Algorithm ends when no elements of array is swapped. After each walk 
    through the array is last element on right place.
    When function returns, the input array is sorted.

    Args:
        arrToSort: Array to be sorted.

    Returns:
        No return value
    """

    isSwapped = True
    lastUnsortedElement = len(arrToSort) - 1

    # After last cycle of the loop, test if some element has been swapped. If no, break the for loop as array 
    # is already sorted
    while isSwapped:
        isSwapped = False        
        # Walk through the array and swap elements if needed
        for currentElement in range(0, lastUnsortedElement):
            if arrToSort[currentElement] > arrToSort[currentElement + 1]:
                arrToSort[currentElement], arrToSort[currentElement + 1] = arrToSort[currentElement + 1], arrToSort[currentElement]
                isSwapped = True
            
        lastUnsortedElement -= 1
        
# Tests        
a = [3, 2, 1,2,1,44,7,88,5,6,99]

print(a)
bubbleSort(a)
print(a)