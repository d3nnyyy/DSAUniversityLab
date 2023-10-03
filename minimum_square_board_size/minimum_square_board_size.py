def get_board_size(w, h, N):

    if w <= h:
        min_side = w
        max_side = N * h
    else:
        min_side = h
        max_side = N * w

    while min_side < max_side:
        mid = (min_side + max_side) // 2

        leaflets_per_row = mid // w
        leaflets_per_col = mid // h
        total_leaflets = leaflets_per_row * leaflets_per_col

        if total_leaflets >= N:
            max_side = mid
        else:
            min_side = mid + 1

    return min_side


print(get_board_size(w=4, h=1, N=12))
print(get_board_size(w=3, h=2, N=10))
print(get_board_size(w=1, h=1, N=4))
print(get_board_size(w=1, h=1, N=5))
print(get_board_size(w=999999999, h=1000000000, N=2))
