import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000000)

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

three, two = 0, 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    now_color = arr[x][y]

    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if arr[nx][ny] == now_color:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            three += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[False for _ in range(n)] for _ in range(n)]


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            two += 1

print(three, two)