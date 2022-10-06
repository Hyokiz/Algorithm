# 14178. 1차원 정원

for t in range(1, int(input()) + 1):
    n, d = map(int, input().split())
    if n % ((d * 2) + 1):
        result = n // ((d * 2) + 1) + 1

    else:
        result = n // (d * 2 + 1)

    print(f'#{t}', result)