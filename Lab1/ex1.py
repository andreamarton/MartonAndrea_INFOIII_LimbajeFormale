
def concatenate(s1, s2):
    return s1 + s2

def invers(s):
    return s[::-1]

def substituie(s, old, new):
    return s.replace(old, new)

def lungime(s):
    return len(s)

if __name__ == "__main__":
    s1 = "abc"
    s2 = "xyz"
    print("Concatenation:", concatenate(s1, s2))
    print("Reverse:", invers(s1))
    print("Substitution:", substituie("abc", "a", "x"))
    print("Length:", lungime(s1))
