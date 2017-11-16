# Accepted
# Python 3

cube = lambda x: x**3  # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    li = []
    fib_0, fib_1 = 0, 1
    for i in range(n):
        li.append(fib_0)
        fib_0, fib_1 = fib_1, fib_0+fib_1

    return li
