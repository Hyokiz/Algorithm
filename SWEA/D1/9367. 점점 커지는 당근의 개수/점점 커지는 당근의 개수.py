t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    c = list(map(int, input().split()))

    cnt = 1
    max_value = 1
    for i in range(n-1):
        if c[i] < c[i+1]:
            cnt += 1

            if max_value < cnt:
                max_value = cnt

        else:
            cnt = 1


    print(f'#{tc} {max_value}')