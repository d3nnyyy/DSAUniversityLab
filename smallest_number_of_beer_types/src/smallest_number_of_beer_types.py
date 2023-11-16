def read_beer_preferences(file_path):
    with open(file_path, 'r') as file:
        num_of_employees, num_of_beers = map(int, file.readline().split())
        preferences_line = file.readline()

    return num_of_employees, num_of_beers, preferences_line


def convert_line_to_binary_array(line):
    mapping = {'Y': 1, 'N': 0}
    line = line.replace(" ", "")
    values = [mapping[char] for char in line]
    binary_array = [values[i:i + 3] for i in range(0, len(values), 3)]

    return binary_array


def transform_preferences(preferences):
    beer_preferences = [[] for _ in range(len(preferences[0]))]

    for employee_idx, preference in enumerate(preferences):
        for beer_idx, likes_beer in enumerate(preference):
            if likes_beer:
                beer_preferences[beer_idx].append(employee_idx + 1)

    return beer_preferences


def min_beers(n, adj):
    beers = set(range(1, len(adj) + 1))
    satisfied_employees = [0] * n

    for beer, employees in enumerate(adj, start=1):
        for emp in employees:
            satisfied_employees[emp - 1] += 1

    for beer, employees in enumerate(adj, start=1):
        if all(satisfied_employees[emp - 1] > 1 for emp in employees):
            beers.discard(beer)

    return len(beers), satisfied_employees


num_of_employees, num_of_beers, preferences_line = read_beer_preferences("input.txt")
array = convert_line_to_binary_array(preferences_line)
adjacency_list_of_beer_preferences = transform_preferences(array)
print(min_beers(num_of_employees, adjacency_list_of_beer_preferences))
