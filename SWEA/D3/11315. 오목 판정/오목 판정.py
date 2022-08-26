# 하 우 좌하 우하
dx = [1, 0, 1, 1]
dy = [0, 1, -1, 1]

def check(omok):
    # 탐색
    for x in range(n):
        for y in range(n):

            # o인 지점부터 델타탐색 시작
            if omok[x][y] == 'o':
                for z in range(4):
                    nx = x
                    ny = y
                    cnt = 0

                    # nx, ny가 범위 내인지 확인하고 o이라면 그 방향으로 쭉 탐색
                    while 0 <= nx < n and 0 <= ny < n and omok[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[z]
                        ny += dy[z]

                    if cnt >= 5:
                        return "YES"

    return "NO"

for t in range(1, int(input()) + 1):
    n = int(input())
    omok = [list(map(str, input())) for _ in range(n)]
    print(f'#{t} {check(omok)}')