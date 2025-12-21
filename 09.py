from shapely.geometry import Polygon, box

with open("09.txt") as file:
    lines = file.read().splitlines()

tiles = list(map(lambda x: list(map(int, x.split(","))), lines))

tile_number = len(tiles)

k = 0

for i in range(tile_number - 1):
    for j in range(i + 1, tile_number):
        tile_i = tiles[i]
        tile_j = tiles[j]

        a = abs(tile_i[0] - tile_j[0]) + 1
        b = abs(tile_i[1] - tile_j[1]) + 1

        k = max(k, a * b)

print(f"Largest area of any rectangle using two red tiles as opposite corners: {k}")

tiles_polygon = Polygon(tiles)

k = 0

for i in range(tile_number - 1):
    for j in range(i + 1, tile_number):
        tile_i = tiles[i]
        tile_j = tiles[j]

        min_tile_x, max_tile_x = sorted([tile_i[0], tile_j[0]])
        min_tile_y, max_tile_y = sorted([tile_i[1], tile_j[1]])

        tiles_rectangle = box(min_tile_x, min_tile_y, max_tile_x, max_tile_y)

        if tiles_polygon.contains(tiles_rectangle):
            a = max_tile_x - min_tile_x + 1
            b = max_tile_y - min_tile_y + 1
            k = max(k, a * b)

print(f"Largest area of any rectangle you can make using only red and green tiles: {k}")
