def nfa_epsilon(input_string):
    state = 0
    i = 0

    while i <= len(input_string):
        if state == 0:
            # q0 -> q1
            state = 1
        elif state == 1:
            # q1 -> q2
            state = 2
        elif state == 2:
            if i < len(input_string) and input_string[i] == 'B':
                # q2 -> q3 pe 'B'
                state = 3
                i += 1
            else:
                return False
        elif state == 3:
            #  q3 -> q4
            state = 4
        elif state == 4:
            if i < len(input_string) and input_string[i] == 'A':
                #  q4 -> q5 pe 'A'
                state = 5
                i += 1
            elif i < len(input_string) and input_string[i] == 'B':
                # q4 -> q6 pe 'B'
                state = 6
                i += 1
            else:
                return False
        elif state == 5 or state == 6:
            #  q5/q6 -> q7
            state = 7
        elif state == 7:
            # q7 -> q8
            state = 8
        elif state == 8:
            if i < len(input_string) and input_string[i] == 'A':
                #  q8 -> q9 pe 'A'
                state = 9
                i += 1
            elif i == len(input_string):
                #  q8 -> q0
                state = 0
            else:
                return False
        elif state == 9:
            return True
        else:
            return False

    return state == 9

test_strings = ["BA", "AB", "BAA"]
for s in test_strings:
    result = "Acceptat" if nfa_epsilon(s) else "Respins"
    print(f"{s}: {result}")
