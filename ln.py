#This function is for count ln(x)
def ln(x):
    res=0; #res store the answer
    j=-1.0; #j store each item of taylor series
    #If x<2, use taylor series to calculate the value		
    if (x<=2):
        for i in range(1,50000):
            j=-j*(x-1);
            res=res+j/i;
        return res;
    #Otherwise, calculate -ln(1/x) to get ln(x) 	
    else:
        return -ln(1.0/x)
