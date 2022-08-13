for t in range(1, int(input()) + 1):
    print(f'#{t}')
    n = int(input())
    for i in range(n):
        print(' '.join(str(11**i)))