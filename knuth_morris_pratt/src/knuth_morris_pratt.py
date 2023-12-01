"""
Knuth-Morris-Pratt algorithm implementation in Python.
"""


def find_pattern_in_string(string: str, pattern: str) -> int:
    """
    Find the index of the first occurrence of the pattern in the string
    using the Knuth-Morris-Pratt algorithm.

    :param string: the text to search in
    :param pattern: the pattern to search for
    :return: the index of the first occurrence of the pattern in the string,
    if not found, -1 is returned
    """
    index_in_string, index_in_pattern = 0, 0

    string_length = len(string)
    pattern_length = len(pattern)

    if pattern_length == 0:
        # If the pattern is empty, it matches at the beginning of the string.
        return 0

    prefix_suffix_array = build_prefix_suffix_array(pattern)

    while index_in_string < string_length:
        if string[index_in_string] == pattern[index_in_pattern]:
            # Matching characters, move both indices.
            index_in_pattern += 1
            index_in_string += 1
            if index_in_pattern == pattern_length:
                return index_in_string - index_in_pattern
        else:
            if index_in_pattern == 0:
                # Mismatch at the beginning of the pattern, move only in the string.
                index_in_string += 1
            else:
                # Mismatch, shift the pattern based on the prefix-suffix array.
                index_in_pattern = prefix_suffix_array[index_in_pattern - 1]

    return -1


def build_prefix_suffix_array(pattern: str) -> list[int]:
    """
    Build the prefix-suffix array for the given pattern.
    It will be used to avoid useless comparisons when a mismatch occurs.

    :param pattern: the pattern to build the prefix-suffix array for
    :return: the prefix-suffix array
    """
    prefix_suffix_array = [0 for _ in pattern]
    current_char, next_char = 0, 1

    for _ in range(len(pattern) - 1):
        if pattern[current_char] == pattern[next_char]:
            prefix_suffix_array[next_char] = current_char + 1
            current_char += 1
            next_char += 1
        else:
            if current_char == 0:
                prefix_suffix_array[next_char] = 0
                next_char += 1
            else:
                current_char = prefix_suffix_array[current_char - 1]
    return prefix_suffix_array
