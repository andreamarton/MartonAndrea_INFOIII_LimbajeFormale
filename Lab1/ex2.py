def concat(s1, s2):
    return s1 + s2

def repeat(s, n):
    return s * n

def reverse(s):
    return s[::-1]

def extract(s, i, j):
    return s[i:j+1]

def replace(s, sub, new_sub):
    return s.replace(sub, new_sub, 1)

if __name__ == "__main__":

    s1 = "abc"
    s2 = "123"
    n = 3
    s = "abcdef"
    i, j = 1, 4
    sub, new_sub = "bc", "XY"

    print("Concatenare:", concat(s1, s2))
    print("Repetare:", repeat(s, n))
    print("Inversare:", reverse(s))
    print("Extragere:", extract(s, i, j))
    print("Înlocuire:", replace(s, sub, new_sub))
