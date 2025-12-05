with open("02.txt") as file:
    lines = file.read().split(",")

k = 0

for line in lines:
    start, end = list(map(int, line.split("-")))

    for id in range(start, end + 1):
        id_string = str(id)
        id_string_length = len(id_string)

        if (
            id_string_length % 2 == 0
            and id_string[: id_string_length // 2] == id_string[id_string_length // 2 :]
        ):
            k += id

print(f"Sum of invalid IDs: {k}")

k = 0

for line in lines:
    start, end = list(map(int, line.split("-")))

    invalid_ids = set()

    for id in range(start, end + 1):
        id_string = str(id)
        id_string_length = len(id_string)

        for i in range(1, id_string_length // 2 + 1):
            if id_string_length % i == 0:
                id_substrings = [
                    id_string[j : j + i] for j in range(0, id_string_length, i)
                ]

                if len(set(id_substrings)) == 1:
                    invalid_ids.add(id)

    k += sum(invalid_ids)

print(f"Sum of invalid IDs (repeated at least twice): {k}")
