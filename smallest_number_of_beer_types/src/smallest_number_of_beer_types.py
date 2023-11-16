"""
Problem Statement

    An outsourcing company is preparing for a corporate party.
    The HR department has sent a questionnaire about the types of beer
    that can be distributed at the party.

    Most of the company's employees like few types of beer,
    and they will be very offended
    if at least one of their favorite beers is not at the party.

    Since you are the market leader, you cannot offend your employees.
    On the other hand, it is expensive to buy all the different types of beer.

    Your task will be to find out how many types of beer
    you will need to bring to the corporate party.

Input Format

    The first line of the input contains two integers, N and B,
    where N is the number of employees and B is the number of beer types.

    The second line contains a string of length N * B + (N - 1),
    where each character is either 'Y' or 'N'.

Output Format

    Print the minimum number of beer types that you need to bring to the corporate party.

Constraints

    Each employee likes at least one type of beer.

    0 < N < 50
    0 < B < 50

Example 1

    Input
        2 2
        YN NY

    Output
        2

    Explanation

        The first employee likes only beer 1,
        and the second employee likes only beer 2,
        so you have to buy two types of beer

Example 2

    Input
        6 3
        YNN YNY YNY NYY NYY NYN

    Output
        2

    Explanation

        Although the majority - four employees - like the third beer,
        it would be best to buy 1 and 2 varieties
"""


def read_beer_preferences(file_path):
    """
    Read the beer preferences from the file.

    The first line of the file contains two integers, N and B,
    where N is the number of employees and B is the number of beer types.

    The second line contains a string of length N * B + (N - 1), where each character is either 'Y' or 'N'.
    The first B characters correspond to the first employee's preferences,
    after which the space is followed by the next B characters
    which correspond to the second employee's preferences, and so on.

    :param file_path:
    :return: a tuple containing the number of employees, the number of beer types,
    and the string of beer preferences
    """
    with open(file_path, 'r') as file:
        # Read the first line of the file.
        num_of_employees, num_of_beers = map(int, file.readline().split())

        # Read the second line of the file.
        preferences_line = file.readline()

    # Return the number of employees, the number of beer types, and the string of beer preferences.
    return num_of_employees, num_of_beers, preferences_line


def convert_line_to_binary_array(line, num_of_beers):
    """
    Convert the string of beer preferences to a binary array.

    :param line: the string of beer preferences, where each character is either 'Y' or 'N'
    :param num_of_beers: the number of beer types
    :return: a binary array of beer preferences
    """

    # Create a mapping from 'Y' to 1 and 'N' to 0.
    mapping = {'Y': 1, 'N': 0}

    # Remove all the spaces from the string of beer preferences.
    line = line.replace(" ", "")

    # Convert the string of beer preferences to a binary array.
    values = [mapping[char] for char in line]

    # Split the binary array into sub-arrays of length `num_of_beers`.
    binary_array = [values[i:i + num_of_beers] for i in range(0, len(values), num_of_beers)]

    # Return the binary array of beer preferences.
    return binary_array


def transform_preferences(preferences):
    """
    Transform the beer preferences into a list of lists,
    where each list contains the employees who like a particular beer.
    :param preferences: a binary array of beer preferences
    :return: a list of lists, where each list contains the employees who like a particular beer
    """

    # Initialize the list of lists.
    # The length of the list is equal to the number of beer types.
    beer_preferences = [[] for _ in range(len(preferences[0]))]

    # Iterate over the binary array of beer preferences.
    # The outer loop iterates over the employees.
    for employee_idx, preference in enumerate(preferences):

        # The inner loop iterates over the beer types.
        for beer_idx, likes_beer in enumerate(preference):

            # If the employee likes the beer,
            # add the employee to the list of employees who like the beer.
            if likes_beer:
                # The employee index is zero-based,
                # so we need to add 1 to the employee index.
                beer_preferences[beer_idx].append(employee_idx + 1)

    # Return the list of lists of beer preferences.
    return beer_preferences


def min_beers(num_of_employees, adjacency_list):
    """
    Find the minimum number of beer types that need to be ordered
    so that each employee will have at least one beer type that they like.

    :param num_of_employees: the number of employees
    :param adjacency_list: a list of lists, where each list contains the employees who like a particular beer
    :return: the minimum number of beer types that need to be ordered
    """

    # Initialize the set of beer types. Each beer type is represented by a unique integer.
    beers = set(range(1, len(adjacency_list) + 1))

    # Initialize the list of satisfied employees.
    # Each element represents the number of beers a specific employee likes.
    satisfied_employees = [0] * num_of_employees

    # Iterate over each beer type and the corresponding list of employees who like that beer.
    for beer, employees in enumerate(adjacency_list, start=1):

        # Iterate over each employee who likes the current beer type.
        for employee in employees:
            # Increment the count of satisfied employees for the current beer type.
            satisfied_employees[employee - 1] += 1

    # Iterate over each beer type and the corresponding list of employees who like that beer.
    for beer, employees in enumerate(adjacency_list, start=1):
        # If all the employees who like the current beer type like more than one beer type
        if all(satisfied_employees[emp - 1] > 1 for emp in employees):
            # Remove the current beer type from the set of beer types.
            beers.discard(beer)

    # Return the number of beer types that need to be ordered.
    return len(beers)


def main():
    file_path = "input.txt"
    num_of_employees, num_of_beers, preferences_line = read_beer_preferences(file_path)
    array = convert_line_to_binary_array(preferences_line, num_of_beers)
    adjacency_list_of_beer_preferences = transform_preferences(array)
    result = min_beers(num_of_employees, adjacency_list_of_beer_preferences)
    print(result)


if __name__ == "__main__":
    main()
