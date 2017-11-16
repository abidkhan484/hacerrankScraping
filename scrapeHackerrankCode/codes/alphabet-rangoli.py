# Accepted
# Python 3

def print_rangoli(size):
    # temp list to check how many letters are used
    temp_li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    li = []

    # loop to append the letters to list
    for i in range(size):
        li.append(temp_li[i])
    del temp_li
    
    # loop to print the first half of the row
    temp = size
    ter_loop = size - 1

    while temp:

        # loop to print the first half of the column
        print((temp*2-2) * '-', end='')
        i = size - 1
        while i >= ter_loop :
            if i != size-1:
                print('-'+li[i], end='')
            else:
                print(li[i], end='')                

            i -= 1

        # loop to print the last half of the column
        i = i + 2
        while i <= size-1:
            print('-'+li[i], end='')
            i += 1

        print((temp*2-2) * '-', end='')
        print()
        temp -= 1
        ter_loop -= 1

    # loop to print the last half of the row
    temp = 1
    ter_loop = 1

    while temp < size:

        #loop to  print the first half of the column
        print((temp*2)*'-', end='')
        i = size - 1
        while i>=ter_loop:
            if i != size-1:
                print('-'+li[i], end='')
            else:
                print(li[i], end='')

            i -= 1

        # loop to print the last half of the column
        i += 2
        while i <= size-1:
            print('-'+li[i], end='')
            i += 1
            
        print((temp*2)*'-', end='')
        print()
        temp += 1
        ter_loop += 1

