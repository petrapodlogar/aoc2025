with open("01.txt") as file:
    lines = file.read().splitlines()

start = 50
n = 100

i = start
k = 0

for line in lines:
    direction, rotations = line[0], int(line[1:])

    if direction == "L":
        i = (i - rotations) % n
    else:
        i = (i + rotations) % n

    if i == 0:
        k += 1

print(f"Number of times the dial is left pointing at 0: {k}")

i = start
k = 0

for line in lines:
    direction, rotations = line[0], int(line[1:])

    for _ in range(rotations):
        if direction == "L":
            i = (i - 1) % n
        else:
            i = (i + 1) % n

        if i == 0:
            k += 1

print(f"Number of times the dial is pointing at 0: {k}")
