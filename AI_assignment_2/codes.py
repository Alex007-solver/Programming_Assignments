def valid_state(j1, j2, j3):
    if j1 < 0 or j1 > 8:
        return 0
    if j2 < 0 or j2 > 5:
        return 0
    if j3 < 0 or j3 > 3:
        return 0
    return 1


def get_next_state(state):
    j1, j2, j3 = state
    children = []
    cap1, cap2, cap3 = 8, 5, 3
    # 1 -> 2
    pour = min(j1, cap2 - j2)
    new = [j1 - pour, j2 + pour, j3]
    if valid_state(*new):
        children.append(new)
    # 1 -> 3
    pour = min(j1, cap3 - j3)
    new = [j1 - pour, j2, j3 + pour]
    if valid_state(*new):
        children.append(new)
    # 2 -> 1
    pour = min(j2, cap1 - j1)
    new = [j1 + pour, j2 - pour, j3]
    if valid_state(*new):
        children.append(new)
    # 2 -> 3
    pour = min(j2, cap3 - j3)
    new = [j1, j2 - pour, j3 + pour]
    if valid_state(*new):
        children.append(new)
    # 3 -> 1
    pour = min(j3, cap1 - j1)
    new = [j1 + pour, j2, j3 - pour]
    if valid_state(*new):
        children.append(new)
    # 3 -> 2
    pour = min(j3, cap2 - j2)
    new = [j1, j2 + pour, j3 - pour]
    if valid_state(*new):
        children.append(new)
    return children


def reset_all(path, temp, curr, children, visited, parent):
    path = []
    curr = []
    children = []
    visited = []
    temp = ()
    parent = {}
    return path, temp, curr, children, visited, parent


initial_state = [8,0,0]
final_state = [4,4,0]

visited = []
parent = {}
path = []
curr = []
children = []
temp = ()

queue = []
queue.append(initial_state)
visited.append(initial_state)
parent[tuple(initial_state)] = None

while queue:
    curr = queue.pop(0)

    if curr == final_state:
        break

    children = get_next_state(curr)

    for i in children:
        if i not in visited:
            queue.append(i)
            visited.append(i)
            parent[tuple(i)] = tuple(curr)

print("BFS Run:")
temp = tuple(final_state)

while temp is not None:
    path.insert(0, temp)
    temp = parent[temp]

print(path)

path, temp, curr, children, visited, parent = reset_all(path, temp, curr, children, visited, parent)

stack = []
stack.append(initial_state)
visited.append(initial_state)
parent[tuple(initial_state)] = None

while stack:
    curr = stack.pop()

    if curr == final_state:
        break

    children = get_next_state(curr)

    for i in children:
        if i not in visited:
            stack.append(i)
            visited.append(i)
            parent[tuple(i)] = tuple(curr)

print("\nDFS Run:")
temp = tuple(final_state)

while temp is not None:
    path.insert(0, temp)
    temp = parent[temp]

print(path)

path, temp, curr, children, visited, parent = reset_all(path, temp, curr, children, visited, parent)


stack = []
limit = 6
found = False

stack.append((initial_state, 0))
visited.append(initial_state)
parent[tuple(initial_state)] = None

while stack:
    curr, depth = stack.pop()

    if curr == final_state:
        found = True
        break

    if depth < limit:
        children = get_next_state(curr)

        for i in children:
            if i not in visited:
                stack.append((i, depth+1))
                visited.append(i)
                parent[tuple(i)] = tuple(curr)

if found:
    print("\nDepth Bounded DFS Run:")
    temp = tuple(final_state)

    while temp is not None:
        path.insert(0, temp)
        temp = parent[temp]

    print(path)
else:
    print("\nDBDFS did not find solution")

path, temp, curr, children, visited, parent = reset_all(path, temp, curr, children, visited, parent)

limit = 0
found = False

while not found:
    visited = []
    parent = {}
    stack = []

    stack.append((initial_state,0))
    visited.append(initial_state)
    parent[tuple(initial_state)] = None

    while stack:
        curr, depth = stack.pop()

        if curr == final_state:
            found = True
            break

        if depth < limit:
            children = get_next_state(curr)

            for i in children:
                if i not in visited:
                    stack.append((i, depth+1))
                    visited.append(i)
                    parent[tuple(i)] = tuple(curr)

    limit += 1

limit -= 1

if found:
    print(f"\nDFID Run (found at limit {limit}):")

    temp = tuple(final_state)

    while temp is not None:
        path.insert(0,temp)
        temp = parent[temp]

    print(path)
else:
    print("\nDFID did not find solution")