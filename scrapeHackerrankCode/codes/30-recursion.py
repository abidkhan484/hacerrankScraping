# Accepted
# Python 3

def factorial(x):
    if(x<=0):
        return 1
    else:
        result = x * factorial(x-1)
        return result

user_input = int(input().strip())
result=1
print(factorial(user_input))

