def check_first_expression(s):
    if not s:
        return False

    #incepe cu 1 sau 00*1
    if s[0] == '1':
        rest = s[1:]
    elif s.startswith("00"):
        i = 0
        while i < len(s) and s[i] == '0':
            i += 1
        if i < len(s) and s[i] == '1':
            rest = s[i+1:]
        else:
            return False
    else:
        return False

    # (0+10*1)*(0+10*1)
    while rest:
        if rest[0] == '0':
            rest = rest[1:]
        elif rest.startswith("10"):
            j = 1
            while j < len(rest) and rest[j] == '0':
                j += 1
            if j < len(rest) and rest[j] == '1':
                rest = rest[j+1:]
            else:
                return False
        else:
            return False
    return True

def check_second_expression(s):
    if not s:
        return False

    # Elimina 0 int
    i = 0
    while i < len(s) and s[i] == '0':
        i += 1

    # Trebuie sa existe cel puțin un '1'
    if i >= len(s) or s[i] != '1':
        return False

    rest = s[i+1:]

    # (0+10*1)*
    while rest:
        if rest[0] == '0':
            rest = rest[1:]
        elif rest.startswith("10"):
            j = 1
            while j < len(rest) and rest[j] == '0':
                j += 1
            if j < len(rest) and rest[j] == '1':
                rest = rest[j+1:]
            else:
                return False
        else:
            return False
    return True

test_strings = ["1","101"]

for s in test_strings:
    first = check_first_expression(s)
    second = check_second_expression(s)
    print(f"{s}: Prima Expresie = {'DA' if first else 'NU'}, A doua Expresie = {'DA' if second else 'NU'}, Echivalente = {'DA' if first == second else 'NU'}")
