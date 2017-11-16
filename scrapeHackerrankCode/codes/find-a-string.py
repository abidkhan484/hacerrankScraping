# Accepted
# Python 3

def count_substring(string, sub_string):
    c = 0; i=0
    while string:
        i = string.find(sub_string)
        if (i>=0):
            c += 1
            string = string[i+1:]
        else:
            break
        
    return c
