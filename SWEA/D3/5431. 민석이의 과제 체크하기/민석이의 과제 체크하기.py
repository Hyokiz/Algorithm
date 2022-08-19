for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    k_list = list(map(int, input().split()))
    submit = []
    print(f'#{t}', end=' ')
    for i in range(1, n+1):
        if i not in k_list:
            submit.append(i)

    for i in submit:
        print(i, end=' ')
    print()