with open("11.txt") as file:
    lines = file.read().splitlines()

edges = dict()

for line in lines:
    start, other = line.split(": ")
    edges[start] = other.split(" ")

start = "you"
end = "out"

k = 0

current_states = [start]

while current_states:
    updated_current_states = []

    for current_state in current_states:
        if end in edges[current_state]:
            k += 1

        updated_current_state = list(filter(lambda x: x != end, edges[current_state]))
        updated_current_states += updated_current_state

    current_states = updated_current_states

print(f"Number of different paths lead from you to out: {k}")

start = "svr"
end = "out"

stop1 = "dac"
stop2 = "fft"

k = 0

current_state_to_count_dict = {(start, False, False): 1}

while len(current_state_to_count_dict) > 0:
    updated_current_state_to_count_dict = dict()

    for current_state_key, current_state_count in current_state_to_count_dict.items():
        current_state, at_stop1, at_stop2 = current_state_key

        if end in edges[current_state] and at_stop1 and at_stop2:
            k += current_state_count

        updated_current_state = list(filter(lambda x: x != end, edges[current_state]))
        for state in updated_current_state:
            state_at_stop1 = at_stop1 or state == stop1
            state_at_stop2 = at_stop2 or state == stop2

            updated_current_state_key = (state, state_at_stop1, state_at_stop2)

            if updated_current_state_key in updated_current_state_to_count_dict:
                updated_current_state_to_count_dict[updated_current_state_key] += current_state_count
            else:
                updated_current_state_to_count_dict[updated_current_state_key] = current_state_count

    current_state_to_count_dict = updated_current_state_to_count_dict

print(f"Number of paths from svr to out that visit both dac and fft: {k}")
