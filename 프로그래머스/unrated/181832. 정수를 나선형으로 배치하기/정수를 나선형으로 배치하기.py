def solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 우하좌상
    x, y = 0, 0
    board[x][y] = 1
    k = 2
    while k <= n ** 2:
        for i, j in zip(dx, dy):
            while True:
                nx, ny = x + i, y + j
                if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] != 0:
                    break
                else:
                    board[nx][ny] = k
                    x, y = nx, ny
                    k += 1
            
    
    return board
                
            