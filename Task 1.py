C=21
F=C*9/5+32
print(F)


s=1.0*10**9
y=s/31536000
print(y)


x=640
i=x/0.0254
f=i/12
y=f/3
m=y/1760
print(i)
print(f)
print(y)
print(m)

A=1000
p=5
n=3
B=A*(1+p/100)**n
print(B)


import math
m=0.0
s=2.0
x=1.0
f=(1/((math.sqrt(2*math.pi))*s))*math.exp((-1.0/2.0)*((x-m)/s)**2)
print(f)


import math
M=67
p=1.038
c=3.7
K=5.4*10**-3
w=100
y=70
T=[4,20]
t_1=(((M**(2.0/3.0))*c*(p**(1.0/3.0)))/(K*(math.pi**2)*((4*math.pi)/3)**(2.0/3.0)))*math.log(0.76*(T[0]-w)/(y-w))
t_2=(((M**(2.0/3.0))*c*(p**(1.0/3.0)))/(K*(math.pi**2)*((4*math.pi)/3)**(2.0/3.0)))*math.log(0.76*(T[1]-w)/(y-w))
print(t_1)
print(t_2)

width=17
height=12.0
dollar='$'
print(width/2)
print(width/2.0)
print(height/3)
print(dollar*5)


import math
r=5
v=(4.0/3.0)*math.pi*r**3
print(v)


import math
R=1.097*10**-2.0
m=1
n=[2,3]
l_1=1/(R*((1/(m**2.0))-(1/(n[0]**2.0))))
l_2=1/(R*((1/(m**2.0))-(1/(n[1]**2.0))))
print(l_1)
print(l_2)


import math
s=100
u=0
a=9.81
t=math.sqrt(2*s/a)
print(t)

