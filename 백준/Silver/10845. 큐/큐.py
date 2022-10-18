from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
q = deque([])

for _ in range(n):
    s = input().split()
    if s[0] == 'push':
        q.append(s[1])

    elif s[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif s[0] == 'size':
        print(len(q))

    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif s[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    else:
        if q:
            print(q[-1])
        else:
            print(-1)
