# 16236. 아기 상어
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y, p = 0, 0, 2
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x, y = i, j

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y, p):
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[0 for _ in range(n)] for _ in range(n)]

    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    fishes = []
    while q:
        curr_x, curr_y = q.popleft()
        for i, j in zip(dx, dy):
            nx, ny = curr_x + i, curr_y + j
            if in_range(nx, ny) and not visited[nx][ny]:
                if arr[nx][ny] <= p:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[curr_x][curr_y] + 1

                    if arr[nx][ny] < p and arr[nx][ny] != 0:
                        fishes.append((nx, ny, distance[nx][ny]))

    fishes.sort(key=lambda x: (x[2], x[0], x[1]))
    return fishes

cnt = 0
result = 0
while True:
    temp = deque(bfs(x, y, p))

    if len(temp) == 0:
        break

    nx, ny, dist = temp.popleft()

    result += dist
    arr[x][y], arr[nx][ny] = 0, 0

    x, y = nx, ny
    cnt += 1

    if cnt == p:
        p += 1
        cnt = 0

print(result)