def mergeSort(arrToSort):
    """Implementation of merge sort algorithm.
    It divides input array in two halves, calls itself for the two halves
    and then merges the two sorted halves.

    Args:
        arrToSort: Array to be sorted

    Returns:
        Sorted array
    """

    # Divide the interval into two halves
    middle = len(arrToSort) // 2

    mergedArr = []

    # Return if there is nothing to sort (only one elemnt to sort is
    # automatically sorted and merged).
    if (len(arrToSort) > 1):
        # Split input array into left and right array
        left = arrToSort[:middle]
        right = arrToSort[middle:]

        # Sort splitted arrays
        left = mergeSort(left)
        right = mergeSort(right)

        # Merge sorted arrays from above lines
        while len(left) > 0 and len(right) > 0:
            if (left[0] > right[0]):
                mergedArr.append(right.pop(0))
            else:
                mergedArr.append(left.pop(0))

        # Add the remaing (not appended) elements of both arrays
        mergedArr += left[:] + right[:]
    else:
        # Return array with length = 1 because it is already sorted
        mergedArr = arrToSort

    return mergedArr


# Tests
a = [88, 9, 4, 9, 3, 2, 4, 1, 77, 25, 5, 5, 6]
print(a)
print(mergeSort(a))