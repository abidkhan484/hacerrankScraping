# Accepted
# Python 3

import re

def fun(s):
    emailRe = r'^[\w-]+@[A-Za-z0-9]+\.[a-zA-z]{,3}$'
    if re.match(emailRe, s):
        return s

