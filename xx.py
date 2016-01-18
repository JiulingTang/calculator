import math
import ln
def xx(x):
    if x<0:
        return "error"
    l=x*ln.ln(x);
    res=0;
    j=1.0;
    q=1.0
    f=1
    m=math.e
    if l<0:
       f=0
       l=-l
    while l>1:
        q=q*math.e
        l=l-1
    for i in range(1,50000):
        res=res+j;
        j=j*l/i;
    if f==1:
        return q*res
    else:
        return 1.0/res/q
