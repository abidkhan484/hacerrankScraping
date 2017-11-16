# Accepted
# Python 3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    total=0
    li = list(student_marks[query_name])

    for i in range(3):
        total += li[i]

    print('%.2f' %(total/3))

