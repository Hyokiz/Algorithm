for t in range(1, int(input()) + 1):
    d, l, n = map(int, input().split())
    result = 0
    for i in range(n):
        result += d * (1 + i * l * 1/100)

    print(f'#{t}', int(result))