# Accepted
# Python 3

import string

m = input().strip(); n = input().strip()
m.lower(); n.lower()
st = list(string.ascii_lowercase)
mList = [0] * 26
nList = [0] * 26

for i in range(len(m)):
    if m[i] in st:
        index = st.index(m[i])
        mList[index] += 1


for i in range(len(n)):
    if n[i] in st:
        index = st.index(n[i])
        nList[index] += 1

count = 0
for i in range(26):
    if mList[i] == nList[i]:
        continue
    else:
        count += (max(mList[i], nList[i]) - min(mList[i], nList[i]))
print(count)

