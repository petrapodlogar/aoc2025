with open("04.txt") as file:
    lines = file.read().splitlines()

diagram = list(map(list, lines))

n = len(lines)
m = len(lines[0])

k = 0

for i in range(n):
    for j in range(m):
        if diagram[i][j] != "@":
            continue

        neighbors = []

        if i - 1 >= 0:
            neighbors += diagram[i - 1][max(j - 1, 0) : min(j + 2, m)]
        if j - 1 >= 0:
            neighbors.append(diagram[i][j - 1])
        if j + 1 < m:
            neighbors.append(diagram[i][j + 1])
        if i + 1 < n:
            neighbors += diagram[i + 1][max(j - 1, 0) : min(j + 2, m)]

        if len(list(filter(lambda x: x == "@", neighbors))) < 4:
            k += 1

print(f"Rolls that can be accessed by forklift: {k}")

removed = set()
check = set()

for i in range(n):
    for j in range(m):
        if diagram[i][j] != "@":
            continue

        neighbors = []

        if i - 1 >= 0:
            for k in range(max(j - 1, 0), min(j + 2, m)):
                neighbors.append((i - 1, k))
        if j - 1 >= 0:
            neighbors.append((i, j - 1))
        if j + 1 < m:
            neighbors.append((i, j + 1))
        if i + 1 < n:
            for k in range(max(j - 1, 0), min(j + 2, m)):
                neighbors.append((i + 1, k))

        if len(list(filter(lambda x: diagram[x[0]][x[1]] == "@", neighbors))) < 4:
            removed.add((i, j))
            check = check.union(set(neighbors))

while len(check) > 0:
    check_i = set()

    for i, j in check:
        if diagram[i][j] != "@" or (i, j) in removed:
            continue

        neighbors = []

        if i - 1 >= 0:
            for k in range(max(j - 1, 0), min(j + 2, m)):
                neighbors.append((i - 1, k))
        if j - 1 >= 0:
            neighbors.append((i, j - 1))
        if j + 1 < m:
            neighbors.append((i, j + 1))
        if i + 1 < n:
            for k in range(max(j - 1, 0), min(j + 2, m)):
                neighbors.append((i + 1, k))

        if (
            len(
                list(
                    filter(
                        lambda x: diagram[x[0]][x[1]] == "@" and x not in removed,
                        neighbors,
                    )
                )
            )
            < 4
        ):
            removed.add((i, j))
            check_i = check_i.union(set(neighbors))

    if len(check_i) == 0:
        break

    check = check_i

print(f"Rolls that can be removed: {len(removed)}")
