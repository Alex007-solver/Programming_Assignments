import itertools

def word_to_value(word, mp):
    return int("".join(str(mp[ch]) for ch in word))

words = [input("Enter first word: "),
         input("Enter second word: "),
         input("Enter result word: ")]
unique_chars = []
for w in words:
    unique_chars += [c for c in w if c not in unique_chars]

solution_found = False

for values in itertools.permutations(range(10), len(unique_chars)):
    
    char_map = dict(zip(unique_chars, values))

    if any(char_map[w[0]] == 0 for w in words):
        continue

    n1, n2, n3 = [word_to_value(w, char_map) for w in words]
    if n1 + n2 == n3:
        solution_found = True
        print("\nSolution:")
        print(f"{n1} + {n2} = {n3}")
        print("Mapping:", char_map)
        break

if not solution_found:
    print("No solution exists")
