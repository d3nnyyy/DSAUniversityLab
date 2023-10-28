def find_num_of_islands(matrix: list[list[int]]) -> int:

    n = len(matrix)
    m = len(matrix[0])

    vis_matrix = [] * n
    for _ in range(m):
        vis_matrix.append([False] * m)

    num = 0

    for i in range(n):
        for j in range(m):
            if not vis_matrix[i][j] and matrix[i][j] == 1:
                num += 1
                dfs(i, j, vis_matrix, matrix)

    return num


def dfs(i, j, vis_matrix, matrix):

    n = len(matrix)
    m = len(matrix[0])

    if i < 0 or i >= n or j < 0 or j >= m or vis_matrix[i][j] or matrix[i][j] == 0:
        return

    vis_matrix[i][j] = True

    delta_row = [1, -1, 0, 0]
    delta_col = [0, 0, 1, -1]

    for d in range(4):

        neighbor_row = delta_row[d] + i
        neighbor_col = delta_col[d] + j

        dfs(neighbor_row, neighbor_col, vis_matrix, matrix)


mat = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1]
]

print(find_num_of_islands(mat))
