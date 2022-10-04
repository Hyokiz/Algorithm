# 11315. 오목 판정

# 하, 우, 좌하, 우하
dx = [1, 0, 1, 1]
dy = [0, 1, -1, 1]

def check(x, y):
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 'o':
                for d in range(4):
                    cnt = 1
                    nx = x + dx[d] * cnt
                    ny = y + dy[d] * cnt

                    while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 'o':
                        cnt += 1
                        nx = x + dx[d] * cnt
                        ny = y + dy[d] * cnt

                    if cnt >= 5:
                        return 'YES'

    return 'NO'

for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    print(f'#{t}', check(0, 0))
