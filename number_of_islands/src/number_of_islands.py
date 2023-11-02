"""
Given a 2D matrix of 1s and 0s,
where 1 represents land and 0 represents water,
find the number of islands in the matrix.

An island is a group of adjacent cells that are all land.
Two cells are adjacent if they are adjacent horizontally, vertically, or diagonally.

Example:
Input:
[
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1]
]

Output: 3

Explanation:
There are 3 islands in the matrix.
The first island is four adjacent 1s in the top-left corner of the matrix,
along with the 1, that's one cell to the bottom-right of it.
The second island is two adjacent 1s in the bottom-right corner of the matrix.
The third island is the 1s in the bottom-left corner of the matrix.
"""


def find_num_of_islands(matrix: list[list[int]]) -> int:
    """
    Finds the number of islands in the matrix.

    Time Complexity:
        The time complexity of this function is O(m * n),
        where 'm' is the number of rows in the matrix and 'n' is the number of columns in the matrix.
        This is due to the use of depth-first search to find the number of islands in the matrix.

    Space Complexity:
        The space complexity is O(m * n) because the visited matrix is the same size as the input matrix.

    :param matrix: a 2D matrix of 1s and 0s
    :return: an integer representing the number of islands in the matrix
    """

    # Check if the matrix is empty
    if not matrix:
        return 0

    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a matrix to keep track of visited cells
    visited = [[False] * cols for _ in range(rows)]

    # Initialize the number of islands
    num_islands = 0

    # Iterate through the matrix
    for i in range(rows):
        for j in range(cols):
            # If the cell is not visited and is part of an island
            if not visited[i][j] and matrix[i][j] == 1:
                # Increment the number of islands and perform depth-first search
                num_islands += 1
                dfs(i, j, visited, matrix)

    return num_islands


def dfs(i, j, visited, matrix):
    """
    Performs depth-first search on the current cell.

    Time Complexity:
        The time complexity of this function is O(1) because the function is only called once for each cell.

    Space Complexity:
        The space complexity is O(1) because the function is only called once for each cell.

    :param i: a row index
    :param j: a column index
    :param visited: a matrix to keep track of visited cells
    :param matrix: the input matrix
    :return:
    """

    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Check if the current cell is out of bounds or already visited, or not part of an island
    if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or matrix[i][j] == 0:
        return

    # Mark the current cell as visited
    visited[i][j] = True

    # Iterate through the neighbors of the current cell
    for delta_row in range(-1, 2):
        for delta_col in range(-1, 2):
            # Find the row and column indices of the neighbor
            neighbor_row = delta_row + i
            neighbor_col = delta_col + j
            # Perform depth-first search on the neighbor
            dfs(neighbor_row, neighbor_col, visited, matrix)
