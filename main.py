import random

x_vals = [0,1,2,3,4,5,6,7,8,9,10]
y_vals = [5,4,3,2,1,0,1,2,3,4,5]
def relu(z):
    return max(0,z)
def drelu(z):
    return 1 if z>0 else 0
def train(x_values, y_values):
    n=10
    w=[random.uniform(-0.5, 0.5) for _ in range(n)]
    v=[random.uniform(-0.5, 0.5) for _ in range(n)]
    b=[random.uniform(-0.5, 0.5) for _ in range(n)]
    for epoch in range(5000):
        for xval,yval in zip(x_values, y_values):
            h=[]
            z=[]
            for i in range(n):
                zi=w[i]*xval+b[i]
                hi=relu(zi)
                h.append(hi)
                z.append(zi)
            y = sum(v[i]*h[i] for i in range(n))
            for i in range(n):
                grad_v = 2*(y-yval)*h[i]
                grad_w = 2*(y-yval)*v[i]*drelu(z[i])*xval
                grad_b = 2*(y-yval)*v[i]*drelu(z[i])
                v[i] -= 0.001*grad_v
                w[i] -= 0.001*grad_w
                b[i] -= 0.001*grad_b
    return w, b, v
def predict(x, w, b, v):
    y=0
    for i in range(len(w)):
        y+=v[i]*relu(w[i]*x+b[i])
    print(y)
w, b, v = train(x_vals, y_vals)
predict(2, w, b, v)
predict(5, w, b, v)
predict(8, w, b, v)
