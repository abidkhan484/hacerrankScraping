# Accepted
# Python 3

if __name__ == '__main__':
    s = input()
    l = len(s)
    
    c, d, e, f, g = (0,) * 5
    for i in range(l):
        if ((s[i].isalnum() is True) and (c!=1)):
            c = 1
        if ((s[i].isalpha() is True) and (d!=1)):
            d = 1
        if ((s[i].isdigit() is True) and (e!=1)):
            e = 1
        if ((s[i].isupper() is True) and (f!=1)):
            f = 1
        if ((s[i].islower() is True) and (g!=1)):
            g = 1

    if c is 1:   
            print('True')
    else:
            print('False')

    if d is 1:   
            print('True')
    else:
            print('False')
            
    if e is 1:   
            print('True')
    else:
            print('False')
            
    if g is 1:   
            print('True')
    else:
            print('False')
            
    if f is 1:   
            print('True')
    else:
            print('False')

