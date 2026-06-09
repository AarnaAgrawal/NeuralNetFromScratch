x_vals=[1,2,3,5,8,10]
y_vals=[3,5,7,11,17,21]
def train(x_values, y_values):
    w1=1.0
    b1=0.0
    w2=1.0
    b2=0.0
    for epoch in range(1000):
        for xval,yval in zip(x_values, y_values):
            h=w1*xval+b1
            y=w2*h+b2
            gradient_w2=2*(y-yval)*h
            gradient_b2=2*(y-yval)
            gradient_w1=2*(y-yval)*w2*xval
            gradient_b1=2*(y-yval)*w2
            w1=w1-0.001*gradient_w1
            b1=b1-0.001*gradient_b1
            w2=w2-0.001*gradient_w2
            b2=b2-0.001*gradient_b2
            print(w1, b1, w2, b2)
    return w1, b1, w2, b2
w1, b1, w2, b2=train(x_vals,y_vals)
print(w1,b1,w2,b2)
print(w2*(w1*18+b1)+b2)
