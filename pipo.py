import math
#The function is to count pi^x
def pipo(x):
    l=x*1.1447298858494001741434273513531;#l=x*ln(pi) 
    res=0;#res is pi power the float part of x*ln(pi)
    j=1.0;
    q=1.0 #q is pi power the integer part of x*ln(pi)
    f=1 #f is a flag to mark if l is positive or negative
    m=math.e
    if l<0:
       f=0 #f=0 means l is negative
       l=-l #If l<0, change l to -l
    while l>1:
        q=q*math.e
        l=l-1
    #after while loop, l is the float part of its original value
    #The for loop implement taylor series to count 
    for i in range(1,50000):
        res=res+j;
        j=j*l/i;
    if f==1:
        return q*res #if x*li(pi) is positive, answer is res*q
    else:
        return 1.0/res/q #otherwise, answer is 1/res/q
