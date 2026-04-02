import networkx as nx
import matplotlib.pyplot as plt

districts = [
    "Adilabad", "Komaram Bheem", "Nirmal", "Mancherial",
    "Nizamabad", "Jagitial", "Peddapalli", "Karimnagar",
    "Rajanna", "Kamareddy", "Medak", "Siddipet",
    "Sangareddy", "Warangal", "Hanamkonda", "Jangaon",
    "Mahabubabad", "Bhadradri", "Khammam", "Suryapet",
    "Nalgonda", "Yadadri", "Medchal", "Hyderabad",
    "Rangareddy", "Vikarabad", "Mahabubnagar",
    "Nagarkurnool", "Wanaparthy", "Jogulamba",
    "Narayanpet", "Mulugu", "Jayashankar"
]

colors = ["Red", "Green", "Blue", "Yellow"]

neighbors = {
    "Adilabad": ["Komaram Bheem", "Nirmal"],
    "Komaram Bheem": ["Adilabad", "Mancherial", "Nirmal"],
    "Nirmal": ["Adilabad", "Nizamabad", "Komaram Bheem", "Mancherial", "Jagtial"],
    "Nizamabad": ["Nirmal", "Kamareddy", "Jagtial"],
    "Kamareddy": ["Nizamabad", "Medak", "Siddipet", "Rajanna", "Sangareddy", "Jagtial"],
    "Medak": ["Kamareddy", "Siddipet", "Sangareddy", "Medchal"],
    "Siddipet": ["Medak", "Karimnagar", "Kamareddy", "Rajanna", "Jangaon", "Hanamkonda", "Yadadri", "Medchal"],
    "Karimnagar": ["Siddipet", "Peddapalli", "Rajanna", "Jagtial", "Jayashankar", "Hanamkonda"],
    "Peddapalli": ["Karimnagar", "Mancherial", "Jagtial", "Jayashankar"],
    "Mancherial": ["Peddapalli", "Komaram Bheem", "Nirmal", "Jagtial", "Jayashankar"],
    "Jagtial": ["Nirmal", "Nizamabad", "Kamareddy", "Rajanna", "Karimnagar", "Peddapalli", "Mancherial"],
    "Rajanna": ["Karimnagar", "Siddipet", "Kamareddy", "Jagtial"],
    "Sangareddy": ["Medak", "Rangareddy", "Kamareddy", "Vikarabad", "Medchal"],
    "Rangareddy": ["Sangareddy", "Hyderabad", "Vikarabad", "Medchal", "Yadadri", "Nalgonda", "Nagarkurnool", "Mahabubnagar"],
    "Hyderabad": ["Rangareddy", "Medchal"],
    "Medchal": ["Hyderabad", "Yadadri", "Siddipet", "Medak", "Sangareddy", "Rangareddy"],
    "Yadadri": ["Medchal", "Nalgonda", "Siddipet", "Jangaon", "Suryapet", "Rangareddy"],
    "Nalgonda": ["Yadadri", "Suryapet", "Rangareddy", "Nagarkurnool"],
    "Suryapet": ["Nalgonda", "Khammam", "Yadadri", "Jangaon", "Mahabubabad"],
    "Khammam": ["Suryapet", "Bhadradri", "Mahabubabad"],
    "Bhadradri": ["Khammam", "Mulugu", "Mahabubabad"],
    "Mulugu": ["Bhadradri", "Jayashankar", "Warangal", "Hanamkonda", "Mahabubabad"],
    "Jayashankar": ["Mulugu", "Warangal", "Peddapalli", "Mancherial", "Karimnagar", "Hanamkonda"],
    "Warangal": ["Jayashankar", "Hanamkonda", "Jangaon", "Mahabubabad", "Mulugu"],
    "Hanamkonda": ["Warangal", "Jangaon", "Siddipet", "Karimnagar", "Jayashankar", "Mulugu"],
    "Jangaon": ["Hanamkonda", "Siddipet", "Yadadri", "Suryapet", "Warangal", "Mahabubabad"],
    "Mahabubabad": ["Warangal", "Jangaon", "Suryapet", "Khammam", "Bhadradri", "Mulugu"],
    "Vikarabad": ["Rangareddy", "Mahabubnagar", "Sangareddy", "Narayanpet"],
    "Mahabubnagar": ["Vikarabad", "Nagarkurnool", "Rangareddy", "Wanaparthy", "Jogulamba", "Narayanpet"],
    "Nagarkurnool": ["Mahabubnagar", "Wanaparthy", "Nalgonda", "Rangareddy"],
    "Wanaparthy": ["Nagarkurnool", "Jogulamba", "Mahabubnagar"],
    "Jogulamba": ["Wanaparthy", "Narayanpet", "Mahabubnagar"],
    "Narayanpet": ["Jogulamba", "Vikarabad", "Mahabubnagar"]
}

def is_safe(district, color, assignment):
    for neighbor in neighbors.get(district, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(assignment):
    if len(assignment) == len(districts):
        return assignment

    for d in districts:
        if d not in assignment:
            district = d
            break

    for color in colors:
        if is_safe(district, color, assignment):
            assignment[district] = color

            result = solve(assignment)
            if result:
                return result

            del assignment[district]

    return None

solution = solve({})

if solution:
    print("Telangana Map Coloring Solution:\n")
    for d in districts:
        print(f"{d} -> {solution[d]}")
else:
    print("No solution found")
    

G = nx.Graph()

for node in neighbors:
    for neighbor in neighbors[node]:
        G.add_edge(node, neighbor)

color_map = [solution.get(node, "gray") for node in G.nodes()]

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)

nx.draw(
    G, pos,
    with_labels=True,
    node_color=color_map,
    node_size=2000,
    font_size=8
)

plt.title("Map Coloring Graph")
plt.show()    
