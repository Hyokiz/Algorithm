# 12221. 구구단2

for t in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    result = -1

    if a > 9 or b > 9:
        pass
    else:
        result = a * b

    print(f'#{t}', result)