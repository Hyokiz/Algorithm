# 1018. 체스판 다시 칠하기

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]
chess = []

for r in range(n - 7):
    for c in range(m - 7):
        i1, i2 = 0, 0
        for i in range(r, r + 8):
            for j in range(c, c + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        i1 += 1

                    else:
                        i2 += 1

                else:
                    if board[i][j] != 'B':
                        i1 += 1

                    else:
                        i2 += 1

        chess.append(i1)
        chess.append(i2)

print(min(chess))