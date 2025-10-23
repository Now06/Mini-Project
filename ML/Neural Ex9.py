import numpy as np

# ---------- Activation ----------
sig = lambda x: 1/(1+np.exp(-x))
dsig = lambda x: x*(1-x)

# ---------- Dataset ----------
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[0],[0],[1]])

# ---------- Initialize weights ----------
np.random.seed(42)
wh, bh = np.random.rand(2,2), np.random.rand(1,2)
wout, bout = np.random.rand(2,1), np.random.rand(1,1)
lr, epochs = 0.5, 10000

# ---------- Training ----------
for _ in range(epochs):
    h = sig(np.dot(X,wh)+bh)
    o = sig(np.dot(h,wout)+bout)
    e = y - o
    d_o = e*dsig(o)
    d_h = d_o.dot(wout.T)*dsig(h)
    wout += h.T.dot(d_o)*lr; bout += np.sum(d_o,0,keepdims=True)*lr
    wh += X.T.dot(d_h)*lr; bh += np.sum(d_h,0,keepdims=True)*lr

# ---------- Testing ----------
for i in X:
    h = sig(np.dot(i,wh)+bh)
    o = sig(np.dot(h,wout)+bout)
    print(f"Input: {i} Output: {o.round()}")
