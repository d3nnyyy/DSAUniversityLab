"""
You are given N leaflets of size W x H.

Write a function that takes the number of leaflets (N),their width (W), and height (H),
and determines the minimum size of a square board needed to accommodate all the leaflets.
The leaflets cannot be rotated or overlapped.

The goal is to find the smallest square board size
that can hold all the leaflets without any excess space.

Example:

    Input: N = 10, W = 2, H = 3
    Output: 9

    Explanation:
        The smallest square board size that can hold all the leaflets is 9.
        The board size of 9 can hold 4 leaflets in each row and 2 leaflets in each column.

    Input: N = 2, W = 1000000000, H = 999999999
    Output: 1999999998

    Explanation:
        The smallest square board size that can hold all the leaflets is 1999999998.
        The board size of 1999999998 can hold 2 leaflets in each row and 1 leaflet in each column.

    Input: N = 5, W = 1, H = 1
    Output: 3

    Explanation:
        The smallest square board size that can hold all the leaflets is 3.
        The board size of 3 can hold 1 leaflet in each row and 1 leaflet in each column.
"""


def get_board_size(w, h, N):
    """
    Finds the minimum size of a square board needed to accommodate all the leaflets.

    :param w: the width of each leaflet
    :param h: the height of each leaflet
    :param N: the number of leaflets
    :return: the minimum size of a square board needed to accommodate all the leaflets

    Time Complexity:
        The time complexity of this function is O(log(max(w, h) * N)),
        where 'w' is the width of each leaflet, 'h' is the height of each leaflet,
        and 'N' is the number of leaflets.
        This is due to the use of binary search to find the minimum size of the square board.

    Space Complexity:
        The space complexity is O(1) because no additional space is used.
    """

    # Initialize the minimum and maximum sides of the square board.
    if w <= h:
        min_side = w
        max_side = N * h
    else:
        min_side = h
        max_side = N * w

    # Use binary search to find the minimum size of the square board.
    while min_side < max_side:

        # Calculate the mid-point of the minimum and maximum sides.
        mid = (min_side + max_side) // 2

        # Calculate the number of leaflets that can fit in each row and column.
        leaflets_per_row = mid // w
        leaflets_per_col = mid // h

        # Calculate the total number of leaflets that can fit in the square board.
        total_leaflets = leaflets_per_row * leaflets_per_col

        # If the total number of leaflets is greater than or equal to the number of leaflets,
        # then the maximum size of the square board is less than or equal to the mid-point.
        if total_leaflets >= N:
            max_side = mid

        # If the total number of leaflets is less than the number of leaflets,
        # then the minimum size of the square board is greater than the mid-point.
        else:
            min_side = mid + 1

    # Return the minimum size of the square board.
    return min_side
