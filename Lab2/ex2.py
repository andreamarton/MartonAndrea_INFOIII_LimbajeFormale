def detect_cat(text):
    state = 0

    for char in text:
        if state == 0:
            if char == 'c':
                state = 1
        elif state == 1:
            if char == 'a':
                state = 2
            elif char == 'c':
                state = 1
            else:
                state = 0
        elif state == 2:
            if char == 't':
                state = 3
                print("Cuvântul 'cat' a fost detectat!")
                return True
            elif char == 'c':
                state = 1
            else:
                state = 0
        elif state == 3:
            return True

    return False

text_input = input("Introdu textul: ")
if detect_cat(text_input):
    print("DA: 'cat' există în text!")
else:
    print("NU: 'cat' nu există în text!")
