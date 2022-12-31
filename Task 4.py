#1)
import numpy as np
def polyfit_file(file, d):
    data = np.loadtxt(file, float)
    x = data[:,0]
    y = data[:,1]
    return np.polyfit(x, y, d)

#2)
import numpy as np
import random as rd
def flip_coin(N):
    h=0.0
    t=0.0
    while h+t<N:
        x=rd.randint(1,2)
        if x==1:
            h+=1
        else:
            t+=1
    if N>10**6:
        return None
    else:
        return h

#3)
import numpy as np
import random as rd
def rolling_dice(n, v):
    attempt=0.0
    doubles=0.0
    while attempt<n:
        x=rd.randint(1,6)
        y=rd.randint(1,6)
        attempt+=1
        if x==y==v:
            doubles+=1
    if n<=10**6.0:
        return doubles
    else:
        return None
def test_throw(n, v):
    if 1<=v<=6 and n<10**6.0:
        prob=rolling_dice(n, v)/n
        return prob
    else:
        return None
 

#4)
import numpy as np
import random as rd
def MCint_pi(N):
    M=0.0
    attempt=0.0
    while attempt<N:
        x=rd.uniform(-1.0, 1.0)
        y=rd.uniform(-1.0, 1.0)
        attempt+=1.0
        if (x**2.0+y**2.0)**(1.0/2.0)<=1:
            M+=1.0
    result=2*2*M/N
    return result

