import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------- Dataset -------------------
data = pd.DataFrame({'x':[1,2,3,5,6,7,8,9],'y':[2,1,4,5,6,7,8,9]})
X = data.to_numpy()

# ------------------- Parameters -------------------
K, max_iters = 2, 10
centroids = X[np.random.choice(len(X), K, replace=False)]

# ------------------- K-Means MapReduce -------------------
for i in range(max_iters):
    assignments = np.argmin(np.linalg.norm(X[:, None] - centroids, axis=2), axis=1)
    centroids = np.array([X[assignments==k].mean(axis=0) if len(X[assignments==k])>0 else X[np.random.randint(len(X))] for k in range(K)])
    print(f"Iteration {i+1} Centroids:\n{centroids}")

# ------------------- Visualization -------------------
plt.scatter(X[:,0], X[:,1], c=assignments, cmap='viridis', s=100)
plt.scatter(centroids[:,0], centroids[:,1], color='red', marker='X', s=200)
plt.title("K-Means Clustering")
plt.show()
