def repeat_until(target, stare):
    while stare < target:
        num = int(input("Introduce 0 sau 1: "))
        if num == 0 and stare == 0:
            stare = 1
        elif num == 1 and stare == 0:
            stare = 2
        elif num == 0 and stare == 1:
            stare = 3
        elif num == 1 and stare == 1:
            stare = 0
        elif num == 1 and stare == 2:
            stare = 3
        elif num == 0 and stare == 2:
            stare = 1

        print("Stare actuala:", stare)

    print("Stare finala:", stare)

repeat_until(3, 0)
