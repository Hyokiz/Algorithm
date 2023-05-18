import sys

input = sys.stdin.readline

T = int(input())
money = [25, 10, 5, 1]
for _ in range(T):
    answer = []
    C = int(input())
    for i in money:
        cnt = C // i
        answer.append(cnt)
        C -= i * cnt
    print(*answer)