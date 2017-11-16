# Accepted
# Python 3

import re
import email.utils as e

R = r'^[a-zA-Z]+[\d\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(int(input().strip())):
    # here i is the input
    i = input()
    # parsed_email is a tuple 
    parsed_email = e.parseaddr(i)
    
    a = re.match(R, parsed_email[1])

    if a:
        print(e.formataddr(parsed_email))


'''
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
'''

