# 12004. 구구단 1

for t in range(1, int(input()) + 1):
    n = int(input())
    result = False

    cnt = 10
    temp = 0
    while True:
        cnt -= 1
        if n % cnt == 0:
            n //= cnt
            cnt = 10
            temp += 1


        if cnt < 2:
            break

        if n == 1 or temp > 1:
            break

    if n == 1:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')