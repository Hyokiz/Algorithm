dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    othello = [[0] * n for _ in range(n)]
    black, white = 0, 0
    othello[n//2-1][n//2-1], othello[n//2][n//2] = 2, 2
    othello[n//2-1][n//2], othello[n//2][n//2-1] = 1, 1
    for _ in range(m):
        row, col, color = map(int, input().split())
        row -= 1
        col -= 1
        othello[row][col] = color

        for d in range(8):
            cnt = 1
            nr = row + dx[d] * cnt
            nc = col + dy[d] * cnt

            while 0 <= nr < n and 0 <= nc < n and othello[nr][nc] != color and othello[nr][nc]:
                cnt += 1
                nr = row + dx[d] * cnt
                nc = col + dy[d] * cnt

            if 0 <= nr < n and 0 <= nc < n and othello[nr][nc] == color:
                for i in range(1, cnt):
                    othello[row + dx[d] * i][col + dy[d] * i] = color

    for r in range(n):
        black += othello[r].count(1)
        white += othello[r].count(2)

    print(f'#{t}', black, white)