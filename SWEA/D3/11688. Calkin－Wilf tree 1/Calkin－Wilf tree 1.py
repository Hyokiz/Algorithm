for t in range(1, int(input()) + 1):
    s = input()
    a, b = 1, 1
    for i in s:
        if i == 'L':
            b += a
        else:
            a += b

    print(f'#{t}', a, b)