# 1970. 쉬운 거스름돈
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


for t in range(1, int(input()) + 1):
    n = int(input())
    result = [0] * 8
    for i in range(8):
        if n == 0:
            break

        if n >= money[i]:
            temp = n // money[i]
            n = n % (money[i] * temp)
            result[i] = temp

    print(f'#{t}')
    print(*result)