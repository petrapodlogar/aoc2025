with open("03.txt") as file:
    lines = file.read().splitlines()

k = 0

for line in lines:
    line_split = list(map(int, list(line)))
    first = max(line_split[:-1])
    second = max(line_split[line_split.index(first) + 1 :])
    k += int(f"{first}{second}")

print(k)

k = 0
n = 12

for line in lines:
    line_split = list(map(int, list(line)))

    selected = []

    for i in range(n - 1):
        selected_i = max(line_split[: (-1) * (n - (i + 1))])
        selected.append(str(selected_i))
        selected_i_index = line_split.index(selected_i)
        line_split = line_split[selected_i_index + 1 :]

    selected.append(str(max(line_split)))

    k += int("".join(selected))

print(k)
