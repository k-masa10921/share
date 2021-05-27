import random
import math

c = 3
k = 9

Ix = range(3)
Iy = range(c)
def value(i):
    return (i+1)*2
def w(i):
    return i+2

def H_value(x):
    return sum(value(i)*x[i] for i in Ix)
def H_penalty(x,y):
    return k*((1-sum(y[i] for i in Iy))**2 + (sum((i+1)*y[i] for i in Iy) - sum(w(i)*x[i] for i in Ix))**2)
def H(x,y):
    return - H_value(x) + H_penalty(x,y)

x = [1,1,1]
y = [1,1,1]

T = 4

for m in range(1000):
    for n in range(1000):
        coin = random.randint(1,6)
        if coin==1:
            D = H(x,y) - H([1-x[0],x[1],x[2]],y)
            if D>0:
                x[0] = 1-x[0]
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    x[0] = 1-x[0]
        elif coin==2:
            D = H(x,y) - H([x[0],1-x[1],x[2]],y)
            if D>0:
                x[1] = 1-x[1]
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    x[1] = 1-x[1]
        elif coin==3:
            D = H(x,y) - H([x[0],x[1],1-x[2]],y)
            if D>0:
                x[2] = 1-x[2]
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    x[2] = 1-x[2]
        elif coin==4:
            D = H(x,y) - H(x,[1-y[0],y[1],y[2]])
            if D>0:
                y[0] = 1-y[0]
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    y[0] = 1-y[0]
        elif coin==5:
            D = H(x,y) - H(x,[y[0],1-y[1],y[2]])
            if D>0:
                y[1] = 1-y[1]
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    y[1] = 1-y[1]
        elif coin==6:
            D = H(x,y) - H(x,[y[0],y[1],1-y[2]])
            if D>0:
                y[2] = 1-y[2]
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    y[2] = 1-y[2]
    if m%100 ==0:
        print('m=',m+1,' : ',x,y,' : ',H(x,y),' : T=',T)
    T*=0.9991
