for t in range(1, int(input()) + 1):
    number = list(map(int, input()))
    reset = False
    cnt = 0
    for i in number:
        if not reset and i == 1:
            cnt += 1
            reset = True
        elif reset and i == 0:
            cnt += 1
            reset = False

    print(f'#{t} {cnt}')