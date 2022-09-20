for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    ans = ''
    for i in range(n):
        if m/2 != m//2:
            ans += '1'
        else:
            ans += '0'
        m //= 2

    if '0' in ans:
        print(f'#{t} OFF')
    else:
        print(f'#{t} ON')
