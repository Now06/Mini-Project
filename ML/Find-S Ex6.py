# Find-S Algorithm Implementation in Python

# Training dataset
# Attributes: [Sky, AirTemp, Humidity, Wind, Water, Forecast]
# Last column: 'Yes' or 'No' (Target)
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Separate attributes and target
X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Initialize hypothesis with the first positive example
for i, val in enumerate(y):
    if val == 'Yes':
        hypothesis = X[i].copy()
        break

# Update hypothesis with remaining positive examples
for i, val in enumerate(y):
    if val == 'Yes':
        for j in range(len(hypothesis)):
            if X[i][j] != hypothesis[j]:
                hypothesis[j] = '?'

print("Most specific hypothesis found by Find-S:")
print(hypothesis)
