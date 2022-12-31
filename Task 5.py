#1)
import math
from scipy.integrate import quad
def gaussian(x,m,s):
    g=(1/((math.sqrt(2*math.pi)*s)))*(math.e)**((-0.5)*((x-m)/s)**2.0)
    if s<=0.0:
        return None
    else:
        return g
def myerror_function(l,h,m,s):
    i=lambda x: gaussian(x,m,s)
    error=quad(i,l,h)
    return error

#2)
import numpy as np
import random
def lorentz_test(A):
    n=np.matrix([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]])
    if np.ma.shape(A)!=(4,4):
        return False
    elif np.allclose(np.linalg.det(A),1.0,0.1)==False:
        return False
    else:
        test_3=np.matrix.transpose(A)*n*A
        return np.allclose(test_3,n,0.01)
