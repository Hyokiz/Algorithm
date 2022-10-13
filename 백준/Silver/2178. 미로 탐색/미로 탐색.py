# 2178. 미로탐색
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
cnt = 1

def bfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))

    return arr[n-1][m-1]

print(bfs(0, 0))