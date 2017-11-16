# Accepted
# Python 3

def capitalize(string):
    #string
    if (string[0]>='a') and (string[0]<='z'):
        string = string[0].upper() + string[1:]
    l = len(string)
    for i in range(1, l):
        if (string[i-1]==' ') and ((string[i]>='a') and (string[i]<='z')):
            string = string[:i]+string[i].upper()+string[i+1:]

            
    return string

