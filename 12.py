with open("12.txt") as file:
    lines = file.read().split("\n\n")

presents = lines[:-1]
regions = lines[-1]

present_shape_dict = dict()
present_size_dict = dict()

for present_data in presents:
    present = present_data.split("\n")
    present_index = int(present[0].replace(":", ""))
    present_shape = present[1:]
    present_shape_dict[present_index] = present_shape
    present_size_dict[present_index] = len(list(filter(lambda x: x == "#", "".join(present_shape))))

k = 0

for region_data in regions.splitlines():
    region = region_data.split(": ")
    region_width, region_length = list(map(int, region[0].split("x")))
    region_presents = region[1].split(" ")
    region_presents_dict = {i: int(present_count) for i, present_count in enumerate(region_presents)}

    region_size = region_width * region_length
    presents_size = 0

    for present in region_presents_dict.keys():
        presents_size += region_presents_dict[present] * present_size_dict[present]

    if region_size < presents_size:
        continue

    k += 1

print(f"Number of regions that can fit all of the presents listed: {k}")
