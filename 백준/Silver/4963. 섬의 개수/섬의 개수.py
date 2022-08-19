import sys
sys.setrecursionlimit(100000)

# 상하좌우 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
# dfs 탐색
def dfs(x, y):
    visited[x][y] = True

    for dir in range(8):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and arr[nx][ny] == 1:
            dfs(nx, ny)

# tc 없이 반복
while True:
    w, h = map(int, input().split())
    # 0, 0이 입력되면 반복문 탈출후 종료
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    result = 0
    # 2차원 배열 탐색
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                result += 1
                dfs(i, j)

    print(result)
