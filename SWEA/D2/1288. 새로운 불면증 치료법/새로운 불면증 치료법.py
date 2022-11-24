for t in range(1, int(input()) + 1):
    n = int(input())
    counter = [0] * 10

    cnt = 1
    while 0 in counter:
        num = str(n * cnt)
        for i in range(len(num)):
            counter[int(num[i])]  += 1
        cnt += 1

    print(f'#{t}', num)