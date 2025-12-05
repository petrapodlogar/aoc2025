with open("05.txt") as file:
    lines = file.read().split("\n\n")

ranges = list(
    map(lambda x: list(map(int, x.replace(" ", "").split("-"))), lines[0].splitlines())
)
ingredients = list(map(int, lines[1].splitlines()))

ranges.sort(key=lambda x: (x[0], x[1]))

k = 0

for ingredient in ingredients:
    for start, end in ranges:
        if ingredient < start:
            break
        if start <= ingredient <= end:
            k += 1
            break

print(f"Number of available ingredients that are fresh: {k}")

while True:
    altered_ranges = [ranges[0]]

    for start, end in ranges[1:]:
        if start <= altered_ranges[-1][1] + 1:
            altered_ranges[-1][1] = max(end, altered_ranges[-1][1])
        else:
            altered_ranges.append([start, end])

    if len(ranges) == len(altered_ranges):
        break

    ranges = altered_ranges
    ranges.sort(key=lambda x: (x[0], x[1]))

k = 0

for start, end in ranges:
    k += end - start + 1

print(f"Number of fresh ingredient IDs: {k}")
