with open("08.txt") as file:
    lines = file.read().splitlines()

junctions = list(map(lambda x: list(map(int, x.split(","))), lines))
junction_number = len(junctions)

n = 1000

distances = dict()

for i in range(junction_number - 1):
    junction_i = junctions[i]

    for j in range(i + 1, junction_number):
        junction_j = junctions[j]

        distance = (
            (junction_i[0] - junction_j[0]) ** 2
            + (junction_i[1] - junction_j[1]) ** 2
            + (junction_i[2] - junction_j[2]) ** 2
        ) ** 0.5
        distances[(min(i, j), max(i, j))] = distance

junction_circuits = {i: i for i in range(junction_number)}

for _ in range(n):
    min_distance = min(distances.values())
    min_distance_junction = list(
        filter(lambda x: distances[x] == min_distance, distances.keys())
    )[0]
    distances.pop(min_distance_junction)

    i, j = min_distance_junction

    old_circuit_i = junction_circuits[i]
    for k in range(junction_number):
        if junction_circuits[k] == old_circuit_i:
            junction_circuits[k] = junction_circuits[j]

circuit_key_count = {i: 0 for i in set(junction_circuits.values())}

for key, value in junction_circuits.items():
    circuit_key_count[value] += 1

circuit_key_counts = list(circuit_key_count.values())
circuit_key_counts.sort(reverse=True)

sizes_multiplied = circuit_key_counts[0] * circuit_key_counts[1] * circuit_key_counts[2]

print(f"Sizes of three largest circuits multiplied: {sizes_multiplied}")

distances = dict()

for i in range(junction_number - 1):
    junction_i = junctions[i]

    for j in range(i + 1, junction_number):
        junction_j = junctions[j]

        distance = (
            (junction_i[0] - junction_j[0]) ** 2
            + (junction_i[1] - junction_j[1]) ** 2
            + (junction_i[2] - junction_j[2]) ** 2
        ) ** 0.5
        distances[(min(i, j), max(i, j))] = distance

junction_circuits = {i: i for i in range(junction_number)}

while len(set(junction_circuits.values())) > 1:
    min_distance = min(distances.values())
    min_distance_junction = list(
        filter(lambda x: distances[x] == min_distance, distances.keys())
    )[0]
    distances.pop(min_distance_junction)

    i, j = min_distance_junction

    old_circuit_i = junction_circuits[i]
    for k in range(junction_number):
        if junction_circuits[k] == old_circuit_i:
            junction_circuits[k] = junction_circuits[j]

x_coordinates_multiplied = junctions[i][0] * junctions[j][0]

print(
    f"X coordinates of last two junction boxes that need to be connected multiplied: {x_coordinates_multiplied}"
)
