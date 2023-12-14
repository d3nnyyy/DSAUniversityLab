import math


def find_longest_wire(gap: int, poles: list[int]) -> float:
    longest_path_to_top = 0
    longest_path_to_bottom = 0

    current_pole = 0

    while current_pole < len(poles) - 1:
        bottom_to_top = longest_path_to_bottom + math.sqrt(gap ** 2 + (poles[current_pole + 1] - 1) ** 2)
        bottom_to_bottom = longest_path_to_bottom + gap
        top_to_top = longest_path_to_top + math.sqrt(
            gap ** 2 + abs(poles[current_pole] - poles[current_pole + 1]) ** 2)
        top_to_bottom = longest_path_to_top + math.sqrt(gap ** 2 + (poles[current_pole] - 1) ** 2)

        longest_path_to_top = max(bottom_to_top, top_to_top)
        longest_path_to_bottom = max(bottom_to_bottom, top_to_bottom)

        current_pole += 1

    return max(longest_path_to_top, longest_path_to_bottom)


print(find_longest_wire(2, [3, 3, 3]))
print(find_longest_wire(4,
                        [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95,
                         97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39,
                         72]))
