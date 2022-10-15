import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = []
queue = deque([])

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                queue.append((i, j, k))

    graph.append(temp)

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()

    for i, j, k in zip(dx, dy, dz):
        nx, ny, nz = x + i, y + j, z + k
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
            queue.append((nx, ny, nz))
            graph[nx][ny][nz] = graph[x][y][z] + 1

cnt = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)

        cnt = max(cnt, max(j))
print(cnt - 1)