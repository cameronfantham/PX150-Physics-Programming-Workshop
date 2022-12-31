#1)
def mysum(l):
    total=0.0
    for n in l:
        total+=n
    return total

#2)
import math
def estimate_pi():
    total=0.0
    k=0.0
    while (math.factorial(4*k)*(1103+26390*k))/(((math.factorial(k))**4.0)*(396)**(4*k))>=1.0*10**-15.0:
        a=(2*math.sqrt(2)/9801)*(math.factorial(4*k)*(1103+26390*k))/(((math.factorial(k))**4.0)*(396)**(4*k))
        k+=1.0
        total+=a
    pi=1/total
    return pi

#3)
import math
def mean_rms_file(file):
    infile=open(file, 'r')
    data=[]
    for line in infile:
        number=float(line)
        data.append(number)
    infile.close()
    total=0.0
    for item in data:
        total+=item
    mean=total/len(data)
    var=0.0
    for item in data:
        q=((item-mean)**2.0)/(len(data)-1)
        var+=q
    x=math.sqrt(var+(mean)**2.0)
    return mean, x

#4)
import math
def trajectory(xdata, v, a):
    g=9.81
    height=[]
    for x in xdata:
        y=x*math.tan(a*math.pi/180)-(1/(2*v**2))*(g*x**2)/(math.cos(a*math.pi/180))**2
        if y>=0:
            height.append(y)
        else:
            height.append(None)
    return height
