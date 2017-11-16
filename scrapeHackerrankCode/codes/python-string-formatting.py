# Accepted
# Python 3

def print_formatted(number):
    p = len(bin(number))-2

    for i in range(1, number+1):
        print(str(i).rjust(p), oct(i)[2:].rjust(p), hex(i)[2:].upper().rjust(p), bin(i)[2:].rjust(p))

