def min_beers(n, adj):
    satisfied_employees = [0] * n
    beers = []

    for beer_idx in range(len(adj)):
        beers.append(beer_idx + 1)
        for emp in adj[beer_idx]:
            satisfied_employees[emp - 1] += 1

    for beer in beers:

        arr = []
        satisfied_employees_copy = [x for x in satisfied_employees]

        for emp in adj[beer - 1]:

            if satisfied_employees_copy[emp - 1] <= 1:
                break

            if satisfied_employees_copy[emp - 1] > 1:
                arr.append(emp - 1)
                satisfied_employees_copy[emp - 1] -= 1

            if len(arr) == len(adj[beer - 1]):
                beers.remove(beer)
                break

    return len(beers), satisfied_employees_copy


# Example 1
n = 6
adj = [[1], [4, 5, 6], [2, 3, 4, 5]]
print(min_beers(n, adj))

# Example 2
n = 2
adj = [[1], [2]]
print(min_beers(n, adj))
