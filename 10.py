from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger

with open("10.txt") as file:
    lines = file.read().splitlines()

machines = list(map(lambda x: x.split(" "), lines))

k = 0


def change_lights_state(state, lights):
    changed_state = list(state)
    for light in lights:
        if state[light] == ".":
            changed_state[light] = "#"
        else:
            changed_state[light] = "."
    return "".join(changed_state)


for machine in machines:
    lights = machine[0][1:-1]
    buttons = machine[1:-1]

    light_number = len(lights)

    button_to_lights_dict = {
        i: set(map(int, button[1:-1].split(","))) for i, button in enumerate(buttons)
    }

    states = {change_lights_state("." * light_number, button_lights) for button_lights in button_to_lights_dict.values()}

    if lights in states:
        k += 1
        continue

    l = 2
    while True:
        states_l = set()
        for state in states:
            for button_lights in button_to_lights_dict.values():
                states_l.add(change_lights_state(state, button_lights))

        if lights in states_l:
            k += l
            break

        states = states_l
        l += 1

print(f"Fewest button presses required to correctly configure the indicator lights on all of the machines: {k}")


k = 0

for machine in machines:
    buttons = list(map(lambda x: tuple(map(int, x[1:-1].split(","))), machine[1:-1]))
    joltage = tuple(map(int, machine[-1][1:-1].split(",")))

    button_number = len(buttons)
    joltage_number = len(joltage)

    joltage_problem = LpProblem("joltage", LpMinimize)
    x = [LpVariable(f"button_{i}", lowBound=0, cat=LpInteger) for i in range(button_number)]
    joltage_problem += lpSum(x)
    for j in range(joltage_number):
        joltage_problem += lpSum(x[i] for i in range(button_number) if j in buttons[i]) == joltage[j]
    joltage_problem.solve()
    machine_k = int(sum(var.varValue for var in x))

    k += machine_k

print(f"Fewest button presses required to correctly configure the joltage level counters on all of the machines: {k}")
