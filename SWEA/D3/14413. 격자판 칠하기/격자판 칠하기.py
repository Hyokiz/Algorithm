# 14413. 격자판 칠하기

def check(odd, even):
    for r in range(n):
        for c in range(m):
            if arr[r][c] == '?':
                continue

            if (r + c) % 2:
                if arr[r][c] != odd:
                    return False
            else:
                if arr[r][c] != even:
                    return False
    return True


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    if check('.', '#') or check('#', '.'):
        print(f'#{t} possible')
    else:
        print(f'#{t} impossible')