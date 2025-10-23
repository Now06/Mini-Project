import pandas as pd, math
from collections import Counter

# ---------- Dataset ----------
data = pd.DataFrame([
 ['Sunny','Hot','High','Weak','No'],
 ['Sunny','Hot','High','Strong','No'],
 ['Overcast','Hot','High','Weak','Yes'],
 ['Rain','Mild','High','Weak','Yes'],
 ['Rain','Cool','Normal','Weak','Yes'],
 ['Rain','Cool','Normal','Strong','No'],
 ['Overcast','Cool','Normal','Strong','Yes'],
 ['Sunny','Mild','High','Weak','No'],
 ['Sunny','Cool','Normal','Weak','Yes'],
 ['Rain','Mild','Normal','Weak','Yes'],
 ['Sunny','Mild','Normal','Strong','Yes'],
 ['Overcast','Mild','High','Strong','Yes'],
 ['Overcast','Hot','Normal','Weak','Yes'],
 ['Rain','Mild','High','Strong','No']], 
 columns=['Outlook','Temperature','Humidity','Wind','Play'])

# ---------- Helper Functions ----------
def entropy(col): c=Counter(col); t=len(col); return -sum((v/t)*math.log2(v/t) for v in c.values())
def info_gain(df,a): t=entropy(df['Play']); return t - sum((len(df[df[a]==v])/len(df))*entropy(df[df[a]==v]['Play']) for v in df[a].unique())

# ---------- ID3 ----------
def id3(df, attrs=None):
    if attrs is None: attrs=list(df.columns[:-1])
    if len(df['Play'].unique())==1: return df['Play'].iloc[0]
    if not attrs: return df['Play'].mode()[0]
    best=max(attrs,key=lambda a: info_gain(df,a))
    return {best:{v:id3(df[df[best]==v].drop(columns=[best]),[a for a in attrs if a!=best]) for v in df[best].unique()}}

tree=id3(data)
print("Decision Tree:", tree)

# ---------- Classify ----------
def classify(tree,ex):
    return ex.get(tree) if not isinstance(tree, dict) else classify(tree[next(iter(tree))].get(ex[next(iter(tree))],None),ex)

new_ex={'Outlook':'Sunny','Temperature':'Cool','Humidity':'High','Wind':'Strong'}
print("New Example Classification:", classify(tree,new_ex))
