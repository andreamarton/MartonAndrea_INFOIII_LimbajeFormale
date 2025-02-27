def bauturi(inputs):
    state = "q0"

    for inp in inputs:
        if state == "q0":
            if inp == "C":
                state = "q1"
            elif inp == "T":
                state = "q2"
            elif inp == "A":
                state = "q3"
            elif inp == "H":
                state = "q4"
            else:
                return False

        elif state in ["q1", "q2", "q3"]:
            if inp == "OK":
                state = "q4"
            else:
                return False

        elif state == "q4":
            print("Comanda finalizata!")
            return True
    return state == "q4"

user_input = input("Introduceti comanda: ").split()

if bauturi(user_input):
    print("Comanda valida!")
else:
    print("Comanda invalida!")
