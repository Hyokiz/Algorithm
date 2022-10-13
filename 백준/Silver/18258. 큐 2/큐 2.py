# 18258. 큐2
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque([])
for _ in range(n):
    s = list(input().split())
    temp = s[0]

    if temp == 'push':
        queue.append(int(s[1]))

    elif temp == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif temp == 'size':
        print(len(queue))

    elif temp == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif temp == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)