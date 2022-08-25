def bfs(x, y):
    visited[x][y] = True
    q = [(x, y)]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and maze[nr][nc] != 1:
                visited[nr][nc] = True
                q.append((nr, nc))

                if maze[nr][nc] == 3:
                    return 1

    return 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(10):
    print(f'#{int(input())}', end=' ')
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    print(bfs(1, 1))