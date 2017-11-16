# Wrong Answer
# Python 3

def buildingList():
    
    n = int(input().strip())
    ar = input()

    for i in range(n):
        p = i+1; pagli = i+1
        print(ar[i])
        while p < n:
            st = ar[i]
            j = pagli
            
            while j < n:
                st += ar[j]
                print(st)
                j += 1

            p += 1
            pagli += 1

for _ in range(int(input().strip())):
    buildingList()

