for t in range(1, int(input()) + 1):
    n = int(input())
    if (n - 2) % 2 == 0:
        print(f'#{t} Alice')
    else:
        print(f'#{t} Bob')