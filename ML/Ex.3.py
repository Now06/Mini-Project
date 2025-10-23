from collections import defaultdict

# ---------- Input Matrices ----------
# Format: (row, col, value)
A = [(0,0,1), (0,1,2),
     (1,0,3), (1,1,4)]

B = [(0,0,5), (0,1,6),
     (1,0,7), (1,1,8)]

# ---------- Mapper ----------
mapped = []

# Map matrix A
for i,j,v in A:
    for col in set(x[1] for x in B):
        mapped.append(( (i,col), ('A', j, v) ))

# Map matrix B
for j,k,v in B:
    for row in set(x[0] for x in A):
        mapped.append(( (row,k), ('B', j, v) ))

# ---------- Shuffle & Sort ----------
shuffle = defaultdict(list)
for key, value in mapped:
    shuffle[key].append(value)

# ---------- Reducer ----------
result = {}
for key, values in shuffle.items():
    a_dict = {j:v for t,j,v in values if t=='A'}
    b_dict = {j:v for t,j,v in values if t=='B'}
    total = sum(a_dict[j]*b_dict[j] for j in a_dict if j in b_dict)
    result[key] = total

# ---------- Output ----------
print("Result of A x B:")
for (i,j), v in sorted(result.items()):
    print(f"({i},{j}) = {v}")
