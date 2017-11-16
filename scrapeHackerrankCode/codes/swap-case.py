# Accepted
# Python 3

def swap_case(s):
    low_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    up_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    vir_s = ''
    l = len(s)
    for i in range(l):
        c=0
        for j in range(26):
            if(s[i]==low_case[j]):
                vir_s += up_case[j]
                c=1
                #print(low_case[j])

            elif (s[i]==up_case[j]):
                vir_s += low_case[j]
                c=1
                #print(up_case[j])

        if(c==0):
            vir_s += s[i]
    return vir_s

