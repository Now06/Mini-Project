import pandas as pd

# ------------------- Load CSV -------------------
data = pd.read_csv("training_data.csv")
X, y = data.iloc[:, :-1].values, data.iloc[:, -1].values

# ------------------- Candidate Elimination -------------------
S = ['0'] * X.shape[1]
G = [['?'] * X.shape[1]]

for i in range(len(X)):
    if y[i] == 'Yes':
        # Generalize S
        S = [S[j] if S[j]==X[i][j] else '?' if S[j]!='0' else X[i][j] for j in range(len(S))]
        # Prune inconsistent G
        G = [g for g in G if all(g[j]=='?' or g[j]==X[i][j] for j in range(len(g)))]
    else:
        # Specialize G
        new_G = []
        for g in G:
            for j in range(len(g)):
                if g[j] == '?':
                    for val in set(X[:,j]) - {X[i][j]}:
                        h = g.copy()
                        h[j] = val
                        new_G.append(h)
                elif g[j] != X[i][j]:
                    new_G.append(g)
        G = new_G

# ------------------- Output -------------------
print("\nMost Specific Hypothesis (S):", S)
print("\nMost General Hypotheses (G):")
for g in G: print(g)
print(f"\nNumber of hypotheses in Version Space: {len(G)}")
