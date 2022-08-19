import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m  and not visited[nx][ny] and arr[nx][ny] == 1:
            dfs(nx, ny)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, int(input()) + 1):
    m, n, k = map(int, input().split())
    # 밭 생성
    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        col, row = map(int, input().split())
        arr[row][col] += 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                result += 1
                dfs(i, j)

    print(result)