t = int(input())
for _ in range(t):
    scores = list(input())
    cnt = 0
    s = 1
    for i in scores:
        if i == 'O':
            cnt += s
            s += 1
        else:
            s = 1

    print(cnt)