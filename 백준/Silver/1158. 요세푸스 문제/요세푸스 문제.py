# 1158. 요세푸스 문제
from collections import deque

n, k = map(int, input().split())
q = deque(list(range(1, n + 1)))
answer = []

while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    answer.append(q.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))