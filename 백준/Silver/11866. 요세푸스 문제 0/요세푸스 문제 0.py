# 11866. 요세푸스 문제 0

n, k = map(int, input().split())
q = list(range(1, n + 1))
answer = []
idx = 0

while q:
    idx += k - 1
    if idx >= len(q):
        idx %= len(q)
    answer.append(str(q.pop(idx)))

print("<", ", ".join(answer), ">", sep="")