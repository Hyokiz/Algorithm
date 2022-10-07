# 4949. 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break

    check = []
    for i in s:
        if i == '(' or i == '[':
            check.append(i)

        elif i == ')':
            if check and check[-1] == '(':
                check.pop()
            else:
                check.append(i)
                break

        elif i == ']':
            if check and check[-1] == '[':
                check.pop()
            else:
                check.append(i)
                break

    if check:
        print('no')
    else:
        print('yes')