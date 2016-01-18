import math

def cosh(x):
    e=2.718281827 
    e_power=e
    #generating absolute value of x
    if(x<0):
        x=x*(-1)	
    if(x!=0):
        #extracting decimal part
        var_x = x - int(x)
        for i in range(0, int(x-1)):
            e_power = e_power*e
    #calculating decimal part's value
        float_power = math.pow(e, var_x)
    #multiplying decimal & non-decimal part to get the whole value
        e_power = e_power*float_power
    else:
        e_power = 1
    ne_power = 1/e_power # calculating the value of e^-x
    cos_h = (e_power + ne_power)/2.0 # cosh(x)
    return cos_h


