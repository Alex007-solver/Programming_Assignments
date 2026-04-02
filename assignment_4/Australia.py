# Map Coloring using CSP (Australia)

# Variables (states)
states = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Domains (colors)
colors = ["Red", "Green", "Blue"]

# Adjacency (neighbors)
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []  # Tasmania has no neighbors
}

# Check if safe to assign color
def is_safe(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def solve(assignment):
    # If all states assigned
    if len(assignment) == len(states):
        return assignment

    # Select unassigned state
    for state in states:
        if state not in assignment:
            break

    # Try all colors
    for color in colors:
        if is_safe(state, color, assignment):
            assignment[state] = color

            result = solve(assignment)
            if result:
                return result

            # Backtrack
            del assignment[state]

    return None

# Solve CSP
solution = solve({})

# Print result
if solution:
    print("Solution:")
    for state in states:
        print(f"{state} -> {solution[state]}")
else:
    print("No solution found")
