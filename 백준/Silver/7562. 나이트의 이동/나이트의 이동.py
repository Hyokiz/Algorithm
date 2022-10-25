from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    dist[sx][sy] = 1
    while q:
        a, b = q.popleft()
        if a == ax and b == ay:
            print(dist[ax][ay] - 1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and dist[x][y] == 0:
                q.append([x, y])
                dist[x][y] = dist[a][b] + 1

t = int(input())
for i in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    dist = [[0] * n for _ in range(n)]
    bfs(sx, sy, ax, ay)