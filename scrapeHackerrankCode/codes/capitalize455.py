# Wrong Answer
# Python 3

def capitalize(string):
    li = string.split()
    l = len(li)
    for i in range(l):
        li[i] = li[i][0].upper()+li[i][1:]

    string = ' '.join(li)

    return string

