dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    othello = [[0] * n for _ in range(n)]
    black, white = 0, 0
    mid = n//2
    othello[mid][mid-1], othello[mid-1][mid] = 1, 1
    othello[mid][mid], othello[mid-1][mid-1] = 2, 2
    for _ in range(m):
        row, col, color = map(int, input().split())
        row -= 1
        col -= 1
        othello[row][col] = color

        for d in range(8):
            cnt = 1
            nr = row + dr[d] * cnt
            nc = col + dc[d] * cnt

            while 0 <= nr < n and 0 <= nc < n and othello[nr][nc] == 3 - color:
                cnt += 1
                nr = row + dr[d] * cnt
                nc = col + dc[d] * cnt

            if 0 <= nr < n and 0 <= nc < n and othello[nr][nc] == color:
                for i in range(1, cnt):
                    othello[row + dr[d] * i][col + dc[d] * i] = color

    for j in range(n):
        black += othello[j].count(1)
        white += othello[j].count(2)

    print(f'#{t}', black, white)