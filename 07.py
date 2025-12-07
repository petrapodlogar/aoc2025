with open("07.txt") as file:
    lines = file.read().splitlines()

k = 0

beams = {lines[0].index("S")}

for line in lines[1:]:
    beams_i = set()

    for beam in beams:
        if line[beam] == "^":
            beams_i = beams_i.union({beam - 1, beam + 1})
            k += 1
        else:
            beams_i.add(beam)

    beams = beams_i

print(f"Times the beam will be split: {k}")

n = len(lines[0])

beams = {i: 0 for i in range(n)}
beams[lines[0].index("S")] = 1

for line in lines[1:]:
    beams_i = {i: 0 for i in range(n)}

    for beam, value in beams.items():
        if line[beam] == "^":
            beams_i[beam - 1] += value
            beams_i[beam + 1] += value
        else:
            beams_i[beam] += value

    beams = beams_i

print(f"Different timelines a single tachyon particle would end up on: {sum(beams.values())}")
