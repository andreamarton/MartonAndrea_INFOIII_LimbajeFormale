def generate_strings(max_length):
    results = []
    for n in range(max_length + 1):
        for m in range(max_length + 1):
            results.append('a' * n + 'b' * m)
    return results

max_length = 5
strings = generate_strings(max_length)

print("Limbaj generat:")
print(" ".join(strings))
