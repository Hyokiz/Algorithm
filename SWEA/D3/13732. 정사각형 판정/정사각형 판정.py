# 13732. 정사각형 판정
from collections import deque
import math

def bfs(queue, arr):
    length = math.sqrt(len(queue))

    if length != int(length):
        return 'no'

    length = int(length)

    x, y = queue.popleft()

    for i in range(x, x + length):
        for j in range(y, y + length):
            if arr[i][j] != '#':
                return 'no'
    return 'yes'



for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    queue = deque()

    for row in range(n):
        for col in range(n):
            if arr[row][col] == '#':
                queue.append((row, col))

    result = bfs(queue, arr)
    
    print(f'#{t}', result)