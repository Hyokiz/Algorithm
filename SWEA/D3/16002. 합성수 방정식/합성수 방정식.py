# 16002. 합성수 방정식

for t in range(1, int(input()) + 1):
    n = int(input())
    x, y = 0, 0
    if n == 1:
        x, y = 9, 8
    else:
        x, y = 3 * n, 2 * n
    print(f'#{t} {x} {y}')