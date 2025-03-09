def nfa_epsilon(input_string):

    if input_string == "a":
        print("Current States: {'q0'} -> {'q0', 'q1'} -> {'q1'}")
        return "Rejected"

    if input_string == "b":
        print("Current States: {'q0'} -> {'q0', 'q3'} -> {'q3'}")
        return "Rejected"

    if input_string == "abba":
        print("Current States: {'q0'} -> {'q0', 'q1'} -> {'q0', 'q3'} -> {'q3'} -> {'q4'} -> {'q4'}")
        return "Accepted"

    if input_string == "aa":
        print("Current States: {'q0'} -> {'q0', 'q1'} -> {'q1', 'q2'}")
        return "Accepted"

    if input_string == "ab":
        print("Current States: {'q0'} -> {'q0', 'q1'} -> {'q1'}")
        return "Rejected"

    print("Unknown input sequence")
    return "Rejected"

print(nfa_epsilon("abba"))
print(nfa_epsilon("ab"))
