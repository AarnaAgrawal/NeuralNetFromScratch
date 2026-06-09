x_vals=[1,2,3,5,8,10]
y_vals=[3,5,7,11,17,21]
def train(x_values, y_values):
    w=1.0
    b=0.0
    for epoch in range(1000):
        for xval,yval in zip(x_values, y_values):
            prediction=w*xval+b
            loss=(prediction-yval)**2
            gradient_w=2*(w*xval+b-yval)*xval
            gradient_b=2*(w*xval+b-yval)
            w=w-0.01*gradient_w
            b=b-0.01*gradient_b
            print(w)
            print(b)
    return w, b
w, b=train(x_vals,y_vals)
print(w)
print(b)
print(18*w+b)
