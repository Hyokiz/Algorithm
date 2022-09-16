def search(r, c):
    cnt = 1
    while True:
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < n and room[nr][nc] - room[r][c] == 1:
                r, c = nr, nc
                cnt += 1
                break
        else:
            return cnt

dx = [-1, 1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우

for t in range(1, int(input()) + 1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    start = []
    values = []
    for i in range(n):
        for j in range(n):
            start.append(room[i][j])
            values.append(search(i, j))

    result = []
    for i in range(n ** 2):
        if max(values) == values[i]:
            result.append(start[i])

    print(f'#{t} {min(result)} {max(values)}')




