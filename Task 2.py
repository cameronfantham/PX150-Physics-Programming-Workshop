#1) 
import math
def c2f(C):
    F=(9.0/5.0)*C+32
    return float(F)

def f2c(F):
    C=(5.0/9.0)*(F-32)
    return float(C)

#2)
import math
def satellite(T):
    G=6.67*(10**-11.0)
    M=5.97*(10**24.0)
    R=6.371*(10**6.0)
    h=(((G*M*T**2.0)/(4*math.pi**2.0))**(1.0/3.0))-R
    if T<=0:
        return None
    elif h<=0:
        return None
    else:
        return h
       
#3)
import math
def p2c(r, t):
    x=r*math.cos(t*math.pi/180)
    y=r*math.sin(t*math.pi/180)
    if r<0:
        return None
    elif t<0 or t>360:
        return None
    else:
        return x, y

#4)
import math
def trprob(E):
    if E==0.0:
        return None
    m=511*10**3.0
    V=9.0
    h=4.135667
    k_1=((2*m*E)**0.5)/h
    k_2=((2*m*(E-V))**0.5)/h
    T=(4*k_1*k_2)/((k_1+k_2)**2)
    R=((k_1-k_2)/(k_1+k_2))**2
    if E<V:
        return None
    else:
        return T, R

#5)
import math
def orbit(l, v):
    G=6.67*10**-11.0
    M=1.9891*10**30
    j=l*v/(0.5*(2*G*M/(v*l)-math.sqrt(((2*G*M/(v*l))**2)+4*(v**2-2*G*M/l))))
    a=0.5*(l+j)
    b=math.sqrt(l*j)
    T=2*math.pi*a*b/(l*v)
    e=(j-l)/(j+l)
    return a, b, T, e
