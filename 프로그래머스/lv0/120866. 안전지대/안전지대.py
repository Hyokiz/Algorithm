dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, 1, -1]
def out_of_range(x, y):
    return not(0 <= x < n and 0 <= y < n)

def solution(board):
    global n
    n = len(board[0])

    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and not visited[i][j]:
                for r, c in zip(dx, dy):
                    nx, ny = i + r, j + c
                    if out_of_range(nx, ny):
                        continue
                    
                    if board[nx][ny] == 0:
                        visited[nx][ny] = True
                        board[nx][ny] = 1
    answer = 0
    for i in range(n):
        answer += board[i].count(0)
    return answer