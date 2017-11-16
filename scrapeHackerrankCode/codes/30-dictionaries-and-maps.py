# Accepted
# Python 3

def nonone(check):
    for j in range(wh):
        if check in my_dic:
            print (check+ "="+ my_dic[check])
            return
            
        else:
            print ("Not found")
            return
            
        j+=1

wh = int(input().strip())

my_dic=dict(input().split() for i in range(wh))

for i in range(wh):
    check = input().strip()
    
    map(nonone(check), check)
            
    i+=1
        
    

