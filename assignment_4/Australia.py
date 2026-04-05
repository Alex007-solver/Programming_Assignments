
states = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

colors = ["Red", "Green", "Blue"]

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [] 
}

def is_safe(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(assignment):

    if len(assignment) == len(states):
        return assignment

    for state in states:
        if state not in assignment:
            break
    for color in colors:
        if is_safe(state, color, assignment):
            assignment[state] = color

            result = solve(assignment)
            if result:
                return result
            del assignment[state]

    return None
solution = solve({})
if solution:
    print("Solution:")
    for state in states:
        print(f"{state} -> {solution[state]}")
else:
    print("No solution found")
