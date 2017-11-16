# Accepted
# Python 3

int_num=int(input())

while(int_num):
    str=input()
    str_len= len(str)
    str1,str2 = "",""
    for i in range(str_len):
        if(i%2==0):
            str1+=str[i]
        else:
            str2+=str[i]
    print(str1,str2)    
    int_num -= 1
