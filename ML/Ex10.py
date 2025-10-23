import pandas as pd, math
from collections import defaultdict

# ---------- Dataset ----------
try: data = pd.read_csv("training_data.csv")
except: data = pd.DataFrame([
 ['Sunny','Hot','High','Weak','No'],
 ['Sunny','Hot','High','Strong','No'],
 ['Overcast','Hot','High','Weak','Yes'],
 ['Rain','Mild','High','Weak','Yes'],
 ['Rain','Cool','Normal','Weak','Yes'],
 ['Rain','Cool','Normal','Strong','No'],
 ['Overcast','Cool','Normal','Strong','Yes'],
 ['Sunny','Mild','High','Weak','No'],
 ['Sunny','Cool','Normal','Weak','Yes'],
 ['Rain','Mild','Normal','Weak','Yes']],
 columns=['Outlook','Temperature','Humidity','Wind','Play'])

X, y = data.iloc[:,:-1], data.iloc[:,-1]
labels = y.unique()
freqs = {c: defaultdict(lambda: defaultdict(int)) for c in labels}

# ---------- Training ----------
for i in range(len(X)):
    for col in X.columns: freqs[y[i]][col][X[col][i]] += 1
priors = {c: sum(y==c)/len(y) for c in labels}
for c in labels:
    for col in X.columns:
        total = sum(freqs[c][col].values()) + len(X[col].unique())
        for val in X[col].unique(): freqs[c][col][val] = (freqs[c][col][val]+1)/total

# ---------- Prediction ----------
def predict(ex):
    probs = {}
    for c in labels:
        prob = math.log(priors[c])
        for col,val in ex.items(): prob += math.log(freqs[c][col].get(val,1e-6))
        probs[c] = prob
    return max(probs,key=probs.get)

# ---------- Test ----------
new_ex = {'Outlook':'Sunny','Temperature':'Cool','Humidity':'High','Wind':'Strong'}
print("Predicted Class:", predict(new_ex))
