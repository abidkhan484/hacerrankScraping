# Accepted
# Python 3

if __name__ == '__main__':
    n = int(input())
    
    if(n%2==0):
        if(((n>1)&(n<6)) | (n>20)):
            print("Not Weird")
            
        else:
            print("Weird")
            
    else:
        print("Weird")

