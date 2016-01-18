#This is the function to get cos(x)
import math
def cos(x):
    x=(x%360+360)%360 #Convert the degree in the range (-360,360)
    #Return the value for the special degree
    if x==0:
        return 1	
    elif x%360==180:
        return -1
    elif x==90 or x==270:
        return 0	
    x=x/180.0*math.pi #Convert degree to radian
    res=1.0; #res store the anwer
    j=1.0; #j store each item of the taylor series
    #Use the for loop to implement taylor series
    for i in range(1,50000):
        j=j*(-1)*x/(2*i-1)
        j=j*x/(2*i)
        res=res+j
    return res;

