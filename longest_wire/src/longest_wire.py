"""
Longest Wire in the Village Problem
"""
import math


def find_longest_wire(gap_width: int, pole_heights: list[int]) -> float:
    """
    Calculate the maximum length of wire needed to connect poles in the village.

    Time complexity: O(n), where n is the number of poles.
    Space complexity: O(1).

    :param gap_width: The width of the gap between the poles.
    :param pole_heights: A list of integers representing the maximum possible height of each pole.
    :return: The maximum length of wire needed to connect the poles.
    """

    # The longest paths to the top and bottom of the current pole.
    longest_path_to_top = 0
    longest_path_to_bottom = 0

    current_pole = 0

    while current_pole < len(pole_heights) - 1:
        # Calculate the longest paths from the bottom of the current pole to the top and bottom of the next pole.
        bottom_to_top = longest_path_to_bottom + math.sqrt(gap_width ** 2 + (pole_heights[current_pole + 1] - 1) ** 2)
        bottom_to_bottom = longest_path_to_bottom + gap_width

        # Calculate the longest paths from the top of the current pole to the top and bottom of the next pole.
        top_to_bottom = longest_path_to_top + math.sqrt(gap_width ** 2 + (pole_heights[current_pole] - 1) ** 2)
        top_to_top = longest_path_to_top + math.sqrt(
            gap_width ** 2 + abs(pole_heights[current_pole] - pole_heights[current_pole + 1]) ** 2)

        # Update the longest paths to the top and bottom of the next pole.
        longest_path_to_top = max(bottom_to_top, top_to_top)
        longest_path_to_bottom = max(bottom_to_bottom, top_to_bottom)

        current_pole += 1

    # Return the longest of the two paths.
    return max(longest_path_to_top, longest_path_to_bottom)
