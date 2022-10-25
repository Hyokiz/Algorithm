for t in range(1, int(input()) + 1):
    n = int(input())
    days = list(map(int, input().split()))
    start = []
    for i in range(7):
        if days[i] == 1:
            start.append(i)

    result = []
    for i in start:
        cnt, day = 0, 0
        while cnt < n:
            day += 1
            if days[i] == 1:
                cnt += 1
            i = (i + 1) % 7
        result.append(day)

    print(f'#{t}', min(result))
