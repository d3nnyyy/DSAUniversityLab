"""
Write a function that takes an unordered array of integers
and returns the range of indices (starting and ending) of the smallest subarray
that needs to be sorted to achieve complete ordering of the entire array.
In case the input array is already sorted, return (-1, -1).

Example:
Input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Output: (3, 9)

Explanation:
The subarray starting at index 3 and ending at index 9 is the smallest subarray
that needs to be sorted to achieve complete ordering of the entire array.

Example:
Input: [1, 2, 3, 4, 5]
Output: (-1, -1)

Explanation:
The input array is already sorted, so return (-1, -1).
"""


def find_shortest_unsorted_subarray(arr):
    """
    Finds the indices of the smallest unsorted subarray in the input array.

    Args:
    arr (list): The input array.

    Returns:
    tuple: A tuple containing two integers, representing the start and end indices of the smallest unsorted subarray.
           If the array is already sorted, (-1, -1) is returned.

    Time Complexity:
    The time complexity of this function is O(n^2), where 'n' is the number of elements in the input array.
    This is due to the use of insertion sort for sorting a copy of the input array.
    But since the input array is almost sorted, the time complexity is closer to O(n).

    Space Complexity:
    The space complexity is O(n) due to the creation of a sorted copy of the input array.
    """

    "Initialize start and end indices for the unsorted subarray."
    x, y = -1, -1

    "Get the length of the input array."
    n = len(arr)

    "Create a copy of the input array to use for sorting."
    sorted_arr = [x for x in arr]

    """
    Sort the copy of the input array using insertion sort. 
    I chose insertion sort because we know that the input array is almost sorted 
    and insertion sort is quite efficient for such cases.
    """
    for i in range(1, n):

        key = sorted_arr[i]
        j = i - 1

        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1

        sorted_arr[j + 1] = key

    """
    Find the first index where the input array and the sorted array differ.
    This is the start index of the unsorted subarray.
    """
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            x = i
            break

    "If the input array is already sorted, return (-1, -1)."
    if x == -1:
        return -1, -1

    """
    Find the last index where the input array and the sorted array differ.
    This is the end index of the unsorted subarray.
    """
    for i in range(n - 1, -1, -1):
        if arr[i] != sorted_arr[i]:
            y = i
            break

    "Return the start and end indices of the unsorted subarray."
    return x, y


# should return (3,9)
print(find_shortest_unsorted_subarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))

# should return (0,4)
print(find_shortest_unsorted_subarray([5, 4, 3, 2, 1]))

# should return (-1,-1)
print(find_shortest_unsorted_subarray([1, 2, 3, 4, 5]))

# should return (-1,-1)
print(find_shortest_unsorted_subarray([1]))

# should return (-1,-1)
print(find_shortest_unsorted_subarray([]))
