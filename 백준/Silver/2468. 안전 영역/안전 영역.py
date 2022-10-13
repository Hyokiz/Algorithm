import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
maxs = sys.maxsize

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_v = 0

def dfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited[x][y] = True

    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            dfs(nx, ny)

ans = 0
for i in range(n):

    if max(arr[i]) > max_v:
        max_v = max(arr[i])

for cnt in range(max_v + 1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if arr[r][c] <= cnt:
                visited[r][c] = True

    temp = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j)
                temp += 1

    if ans < temp:
        ans = temp

print(ans)