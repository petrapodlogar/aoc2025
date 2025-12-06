with open("06.txt") as file:
    lines = file.read().splitlines()

lines = list(map(lambda x: " ".join(x.split()), lines))
lines = list(map(lambda x: x.split(" "), lines))

values = list(map(lambda x: list(map(int, x)), lines[:-1]))
operations = lines[-1]

k = 0

for i in range(len(operations)):
    if operations[i] == "+":
        k_i = 0
    else:
        k_i = 1

    for line in values:
        if operations[i] == "+":
            k_i += line[i]
        else:
            k_i *= line[i]

    k += k_i

print(f"Grand total found by adding together all of the answers to the individual problems: {k}")

with open("06.txt") as file:
    lines = file.read().splitlines()

values = lines[:-1]

n = max(list(map(len, lines)))

values = list(map(lambda x: x + " " * (n - len(x)), values))
values = list(zip(*values))
values = list(map(lambda x: "".join(x).replace(" ", ""), values))

k = 0

for operation in operations:
    if operation == "+":
        k_i = 0
    else:
        k_i = 1

    j = 0
    for value in values:
        if value != "":
            if operation == "+":
                k_i += int(value)
            else:
                k_i *= int(value)
            j += 1
        else:
            break

    k += k_i
    values = values[j + 1:]

print(f"Grand total found by adding together all of the answers to the individual problems (columns): {k}")
