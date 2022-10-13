# 7576. 토마토
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = -1
queue = deque()


def is_out_of_range(x, y):
    return not (0 <= x < n and 0 <= y < m)


def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j

            if is_out_of_range(nx, ny):
                continue

            if arr[nx][ny] < 0:
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] += arr[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))

bfs()
flag = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = -1
            flag = True
            break
        if arr[i][j] - 1 > ans:
            ans = arr[i][j] - 1

    if flag:
        break

print(ans)