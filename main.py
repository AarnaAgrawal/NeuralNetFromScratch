x_vals=[1,2,3,5,8,10]
y_vals=[2,4,6,10,16,20]
def train(x_values, y_values):
    w=1.0
    for epoch in range(1000):
        for xval,yval in zip(x_values, y_values):
            prediction=w*xval
            loss=(prediction-yval)**2
            gradient=2*(w*xval-yval)*xval
            w=w-0.01*gradient
            print(w)
    return w
print(train(x_vals, y_vals)*16)
