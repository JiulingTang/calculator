#This function count the root square of a number x
import sys
import math
def sqrt(x):
    if x<0:
        return "error"
    l=0
    r=1.3407807929942596e+154
    while math.fabs(l-r)>=0.00001:
           m=(l+r)/2.0 #m is the average of l and r
           if m*m>x:
               r=m #if m^2>x, the range is [l,m]
           else:
               l=m #if m^m<=x, the range is [m,r]
    return l
