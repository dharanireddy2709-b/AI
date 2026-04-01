# Telangana Map Coloring using CSP (Backtracking)

districts = ["Hyderabad", "Rangareddy", "Medchal", "Karimnagar",
             "Peddapalli", "Rajanna Sircilla", "Nalgonda",
             "Suryapet", "Khammam", "Bhadradri"]

colors = ["Red", "Green", "Blue"]

# Neighbouring districts
neighbors = {
    "Hyderabad": ["Rangareddy", "Medchal"],
    "Rangareddy": ["Hyderabad", "Medchal"],
    "Medchal": ["Hyderabad", "Rangareddy"],
    "Karimnagar": ["Peddapalli", "Rajanna Sircilla"],
    "Peddapalli": ["Karimnagar"],
    "Rajanna Sircilla": ["Karimnagar"],
    "Nalgonda": ["Suryapet"],
    "Suryapet": ["Nalgonda", "Khammam"],
    "Khammam": ["Suryapet", "Bhadradri"],
    "Bhadradri": ["Khammam"]
}

# Check if color assignment is valid
def check_valid(district, color, result):
    for n in neighbors[district]:
        if n in result and result[n] == color:
            return False
    return True

# Backtracking function
def solve(result):
    
    # if all districts are colored
    if len(result) == len(districts):
        return True
    
    # pick next unassigned district
    for d in districts:
        if d not in result:
            
            for c in colors:
                if check_valid(d, c, result):
                    result[d] = c
                    
                    if solve(result):
                        return True
                    
                    # backtrack
                    result.pop(d)
            
            return False

# Run
result = {}
solve(result)

# Print output
print("\nTelangana Map Coloring:\n")
for d in result:
    print(d, "->", result[d])
