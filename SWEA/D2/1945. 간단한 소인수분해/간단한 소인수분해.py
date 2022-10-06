# 1945. 간단한 소인수분해
def division(n, x):
    temp = 0
    while n % x == 0:
        n //= x
        temp += 1
    result.append(temp)
    return


for t in range(1, int(input()) + 1):
    n = int(input())
    result = []

    division(n, 2)
    division(n, 3)
    division(n, 5)
    division(n, 7)
    division(n, 11)

    print(f'#{t}', *result)