# Accepted
# Python 3

def minion_game(st):
    stuart = 0
    kevin = 0

    l = len(st)
    
    for i in range(l):
        if st[i] in 'AEIOU':
            # here l is the length of the string
            kevin += (l-i)
        else:
            stuart += (l-i)
    
    if stuart==kevin:
        print('Draw')
    elif stuart==max(stuart, kevin):
        print('Stuart', stuart)
    else:
        print('Kevin', kevin)

