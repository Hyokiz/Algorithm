for t in range(1, int(input()) + 1):
    n = int(input())
    print(f'#{t}', end=' ')
    if (n - 2) % 2 == 0:
        print('Alice')
    else:
        print('Bob')