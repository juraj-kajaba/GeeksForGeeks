def mergeSortModif(arrToSort, start, end):
    """Implementation of merge sort algorithm.
    It divides input array in two halves, calls itself for the two halves
    and then merges the two sorted halves.
    Modified because contains additional input parameter start and end index of the input array

    Args:
        arrToSort: Array to be sorted
        start: starting index of the array
        end: ending index of the array

    Returns:
        Sorted array
    """

    # Divide the interval into two halves
    middle = (end-start) // 2

    mergedArr = []

    if (end == start):
        mergedArr.append(arrToSort[start])
    else:
        # Sort splitted arrays
        if (end - start > 1):
            left = mergeSortModif(arrToSort, start, start + middle-1)
            right = mergeSortModif(arrToSort, start + middle, end)
        else:
            left = [arrToSort[start]]
            right = [arrToSort[end]]            


        # Merge sorted arrays from above lines
        leftCurrent = 0
        leftEnd = len(left)
        rightCurrent = 0
        rightEnd = len(right)


        # Both arrays must contain some not included element otherwise skip loop
        while(rightCurrent < rightEnd and leftCurrent < leftEnd):
            if(left[leftCurrent] > right[rightCurrent]):
                mergedArr.append(right[rightCurrent])
                rightCurrent += 1
            else:
                mergedArr.append(left[leftCurrent])
                leftCurrent += 1

        # Add the remaing (not appended) elements of left arrays
        while(leftCurrent < leftEnd):
            mergedArr.append(left[leftCurrent])
            leftCurrent += 1

        # Add the remaing (not appended) elements of left arrays
        while(rightCurrent < rightEnd):
            mergedArr.append(right[rightCurrent])
            rightCurrent += 1

    return mergedArr


# Tests
a = [88, 9,22,18,18,2,33,74,54,46,23,77,87,45,45,87,4,0,5,7,0]
#a = [88, 9,44]

print(a)
print(mergeSortModif(a,0,len(a) - 1))