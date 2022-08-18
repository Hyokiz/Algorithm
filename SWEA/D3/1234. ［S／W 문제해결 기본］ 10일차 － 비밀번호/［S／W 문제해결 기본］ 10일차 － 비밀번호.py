for t in range(1, 11):
    times, numbers = input().split()
    stack = []
    print(f'#{t} ', end='')
    for i in numbers:
        if i not in stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    for i in stack:
        print(i, end='')
    print()