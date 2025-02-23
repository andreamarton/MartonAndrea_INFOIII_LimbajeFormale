alfabet = {'a', 'b', 'c', 'd'}

def verifica_cuvant(cuvant):
    if len(cuvant) > 6:
        return False

    perechi = 0
    i = 0
    while i < len(cuvant) - 1:
        if cuvant[i] == cuvant[i + 1]:
            perechi += 1
            i += 2
        else:
            i += 1

    return perechi == 3

def dfa(cuvant):
    stare = 0
    for litera in cuvant:
        if litera not in alfabet:
            return False
        if stare == 0 and litera in alfabet:
            stare = 1
        elif stare == 1 and litera in alfabet:
            stare = 2
        elif stare == 2 and litera in alfabet:
            stare = 3
        elif stare == 3 and litera in alfabet:
            stare = 3

    return stare == 3

cuvinte = ["aabbcc", "aaa", "bbbacc"]
for cuvant in cuvinte:
    apartine = verifica_cuvant(cuvant)
    automat = dfa(cuvant)
    print(f"Cuvântul '{cuvant}' respectă regulile: {apartine}, DFA: {automat}")
