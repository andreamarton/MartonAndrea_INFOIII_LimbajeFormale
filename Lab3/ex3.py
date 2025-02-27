initial_states = {"q0"}
final_states = {"q2"}

def nfa(input_string):
    current_states = initial_states

    for char in input_string:
        next_states = set()

        if "q0" in current_states:
            if char == "0":
                next_states.update(["q0", "q1", "q2"])
            elif char == "1":
                next_states.update(["q1", "q2"])

        if "q1" in current_states:
            if char == "0":
                next_states.update(["q1", "q2"])
            elif char == "1":
                next_states.update(["q2"])

        if "q2" in current_states:
            if char == "0" or char == "1":
                next_states.add("q2")

        current_states = next_states

    return not current_states.isdisjoint(final_states)

test_strings = ["01"]
for string in test_strings:
    print(f"Input: {string} => Acceptat: {nfa(string)}")
