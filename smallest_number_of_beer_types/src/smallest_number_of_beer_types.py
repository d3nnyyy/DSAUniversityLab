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

INVALID_PREFERENCES_LINE_MSG = "The number of characters in the preferences line is invalid."
INVALID_NUM_OF_EMPLOYEES_MSG = "The number of employees must be between 0 and 50."
INVALID_NUM_OF_BEERS_MSG = "The number of beer types must be between 0 and 50."
NO_BEER_PREFERENCE_MSG = "Each employee must like at least one type of beer."


def execute_beer_preferences(file_path: str) -> str | int:
    """
    Execute the beer preferences logic, including reading from the file and handling constraints.

    :param file_path: the path to the input file
    :return: the minimum number of beer types that need to be ordered or an error message
    """
    try:
        # Read beer preferences from the file
        num_of_employees, num_of_beers, preferences_line = read_beer_preferences(file_path)

        # Check if the number of employees is within the allowed range
        if not 0 < num_of_employees < 50:
            return INVALID_NUM_OF_EMPLOYEES_MSG

        # Check if the number of beer types is within the allowed range
        if not 0 < num_of_beers < 50:
            return INVALID_NUM_OF_BEERS_MSG

        # Check if the preferences line is valid
        if not len(preferences_line) == num_of_employees * num_of_beers + (num_of_employees - 1):
            return INVALID_PREFERENCES_LINE_MSG

        # Convert the string of beer preferences to a binary array
        array = convert_line_to_binary_array(preferences_line, num_of_beers)

        # Transform beer preferences into a list of lists
        adjacency_list_of_beer_preferences = transform_preferences(array)

        # Calculate the minimum number of beer types
        result = min_beers(num_of_employees, adjacency_list_of_beer_preferences)

        return result
    except Exception as e:
        return str(e)


def read_beer_preferences(file_path: str) -> tuple:
    """
    Read the beer preferences from the file.

    The first line of the file contains two integers, N and B,
    where N is the number of employees and B is the number of beer types.

    The second line contains a string of length N * B + (N - 1),
    where each character is either 'Y' or 'N'.
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


def convert_line_to_binary_array(line: str, num_of_beers: int) -> list[list[int]]:
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


def transform_preferences(preferences: list[list[int]]) -> list[list[int]]:
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


def min_beers(num_of_employees: int, adjacency_list: list[list[int]]) -> str | int:
    """
    Find the minimum number of beer types that need to be ordered
    so that each employee will have at least one beer type that they like.

    :param num_of_employees: the number of employees
    :param adjacency_list: a list of lists,
    where each list contains the employees who like a particular beer
    :return: the minimum number of beer types that need to be ordered
    """

    # Create a set of all employees who like at least one beer.
    liked_beers_set = set(employee for employees in adjacency_list for employee in employees)

    # If there is an employee who does not like any beer, return an error message.
    if not set(range(1, num_of_employees + 1)).issubset(liked_beers_set):
        return NO_BEER_PREFERENCE_MSG

    # Initialize the set of beer types. Each beer type is represented by a unique integer.
    beers = set(range(1, len(adjacency_list) + 1))

    # Initialize the list of satisfied employees.
    # Each element represents the number of beers a specific employee likes.
    satisfied_employees = [0] * num_of_employees

    # Iterate over each beer type and the corresponding list of employees who like that beer.
    for beer, employees in enumerate(adjacency_list, start=1):

        # Check if there is at least one beer liked by each employee.
        if not all(any(employee in beer_preferences for beer_preferences in adjacency_list) for employee in employees):
            # Return the number of beer types that need to be ordered.
            return len(beers)

        # Iterate over each employee who likes the current beer type.
        for employee in employees:
            # Increment the count of satisfied employees for the current beer type.
            satisfied_employees[employee - 1] += 1

    # Iterate over each beer type and the corresponding list of employees who like that beer.
    for beer, employees in enumerate(adjacency_list, start=1):
        # If all the employees who like the current beer type like more than one beer type
        if all(satisfied_employees[employee - 1] > 1 for employee in employees):
            # Remove the current beer type from the set of beer types.
            beers.discard(beer)
            # Update the count of satisfied employees for the current beer type.
            for employee in employees:
                satisfied_employees[employee - 1] -= 1

    # Return the number of beer types that need to be ordered.
    return len(beers)
