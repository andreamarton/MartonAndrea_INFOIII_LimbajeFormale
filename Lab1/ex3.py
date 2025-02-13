
def generatePalindromes(alphabet, max_length):
    palindromes = {i: [] for i in range(1, max_length + 1)}

    def backtrack(current):
        if len(current) > max_length:
            return
        if current == current[::-1]:
            palindromes[len(current)].append(current)
        for char in alphabet:
            backtrack(current + char)

    for char in alphabet:
        backtrack(char)

    return palindromes

alphabet = ['0', '1', '2']
max_length = 5
palindromes = generatePalindromes(alphabet, max_length)

for length in range(1, max_length + 1):
    print(f"Palindroame de lungime {length}:")
    for p in palindromes[length]:
        print(p)
    print()
