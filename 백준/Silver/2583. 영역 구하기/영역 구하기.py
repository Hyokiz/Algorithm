# 2583. 영역 구하기
import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

def dfs(y, x, cnt):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    arr[y][x] = 2

    for i, j in zip(dx, dy):
        ny, nx = y + i, x + j

        if 0 <= ny < m and 0 <= nx < n and arr[ny][nx] == 0:
            cnt = dfs(ny, nx, cnt + 1)

    return cnt

ans = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            ans.append(dfs(i, j, 1))

print(len(ans))
print(*sorted(ans))
