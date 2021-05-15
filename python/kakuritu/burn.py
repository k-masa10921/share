import random
import math
def f(x,y,z):
    return 7*x + 12*y + 16*z - 4*x*y - 8*x*z - 16*y*z

T = 10

x = 1
y = 1
z = 0

for m in range(50):
    for n in range(50):
        coin = random.randint(1,3)
        if coin==1:
            D = f(x,y,z) - f(1-x,y,z)
            if D>0:
                x = 1-x
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    x = 1-x
        elif coin==2:
            D = f(x,y,z) - f(x,1-y,z)
            if D>0:
                y = 1-y
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    y = 1-y
        else:
            D = f(x,y,z) - f(x,y,1-z)
            if D>0:
                z = 1-z
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    z = 1-z
    print('m=',m+1,' : ',x,y,z,' : ',f(x,y,z),' : T=',T)
    T*=0.9
