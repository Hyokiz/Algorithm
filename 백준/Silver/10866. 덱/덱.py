# 10866. 덱
from collections import deque
import sys

n = int(input())
q = deque([])

for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "push_front":
        q.appendleft(s[1])
    elif s[0] == "push_back":
        q.append(s[1])
    elif s[0] == "pop_front":
        print(q.popleft() if q else -1)
    elif s[0] == "pop_back":
        print(q.pop() if q else -1)
    elif s[0] == "size":
        print(len(q))
    elif s[0] == "empty":
        print(0 if q else 1)
    elif s[0] == "front":
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)