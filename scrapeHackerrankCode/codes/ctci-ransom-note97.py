# Accepted
# Python 3

def ransom_note(magazine, ransom):
    magazine.sort()
    ransom.sort()
    j = 0

    for i in range(len(magazine)):
        try:
            if magazine[i]==ransom[j]:
                j += 1
        except:
            break

    if j==len(ransom):
        return True
    else:
        return False

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

