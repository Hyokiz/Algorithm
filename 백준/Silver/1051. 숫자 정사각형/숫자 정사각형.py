# 1051. 숫자 정사각형

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
max_length = min(n, m)
answer = 0

for i in range(max_length, 0, -1):
    for r in range(n - i + 1):
        for c in range(m - i + 1):
            a, b, c, d = board[r][c], board[r][c + (i - 1)], board[r + (i - 1)][c], board[r + (i - 1)][c + (i - 1)]
            if a == b and b == c and c == d:
                answer = i ** 2
                break

        if answer: break

    if answer: break

print(answer)