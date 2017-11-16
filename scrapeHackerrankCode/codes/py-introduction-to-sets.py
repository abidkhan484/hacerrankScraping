# Accepted
# Python 3

def average(array):
    array=list(set(array))
    l=len(array)
    total=0
    
    for i in range(l):
        total+=array[i]

    return total/l
