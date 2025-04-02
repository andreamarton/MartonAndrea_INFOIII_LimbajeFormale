def uniune(L1, L2):
    return list(set(L1) | set(L2))

def intersectie(L1, L2):
    return list(set(L1) & set(L2))

def concatenare(L1, L2):
    return [x + y for x in L1 for y in L2]

def diferenta(L1, L2):
    return list(set(L1) - set(L2))

def invers(L1,L2):
    return list(reversed(list(set(L1) | set(L2))))

def menu():


    L1 = []
    L2 = []

    print("Limbajul L1:")
    while True:
        word = str(input())
        if word == "":
             break
        else:
            L1.append(word)

    print("Limbajul L2:")
    while True:
        word = str(input())
        if word == "":
            break
        else:
            L2.append(word)

    while True:
        print("\nAlege o operatie:")
        print("1. Uniune")
        print("2. Intersectie")
        print("3. Concatenare")
        print("4. Diferenta L1 - L2")
        print("5. Invers")

        print("6. Iesire")

        optiune = input("Optiunea: ")

        if optiune == "1":
            print( uniune(L1, L2))
        elif optiune == "2":
            print(intersectie(L1, L2))
        elif optiune == "3":
            print( concatenare(L1, L2))
        elif optiune == "4":
            print( diferenta(L1, L2))
        elif optiune == "5":
            print( invers(L1, L2))
        elif optiune == "6":
            break
        else:
            print("Optiune invalida!")

if __name__ == "__main__":
    menu()
