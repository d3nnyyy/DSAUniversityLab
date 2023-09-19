def find_shortest_unsorted_subarray(arr):
    x, y = -1, -1
    n = len(arr)
    sorted_arr = [x for x in arr]

    for i in range(1, n):

        key = sorted_arr[i]
        j = i - 1

        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1

        sorted_arr[j + 1] = key

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            x = i
            break

    if x == -1:
        return -1, -1

    for i in range(n - 1, -1, -1):
        if arr[i] != sorted_arr[i]:
            y = i
            break

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
