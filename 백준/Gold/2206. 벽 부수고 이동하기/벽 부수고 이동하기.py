# 2206. 벽 부수고 이동하기
from collections import deque
import sys

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    q = deque([])
    q.append((0, 0, 1))
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        x, y, wall = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j

            if in_range(nx, ny):
                if arr[nx][ny] == 1 and wall == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx, ny, 0))

                elif arr[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))

    return -1

print(bfs())