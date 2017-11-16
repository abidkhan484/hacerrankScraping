# Accepted
# Python 3

def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4==0):
        if(year%400==0):
            leap=True
            
        elif(year%100==0):
            leap=False
            
        else:
            leap= True
        
    return leap
