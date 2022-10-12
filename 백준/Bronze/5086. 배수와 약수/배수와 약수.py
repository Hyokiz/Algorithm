ans = 'neither'
while True:
    n, m = map(int, input().split())
    if n == m:
        break

    if n > m:
        if n % m == 0:
            print('multiple')
        else:
            print(ans)
    else:
        if m % n == 0:
            print('factor')
        else:
            print(ans)