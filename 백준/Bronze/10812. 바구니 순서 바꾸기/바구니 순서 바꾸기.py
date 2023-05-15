import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = list(range(1, n + 1))

for _ in range(m):
    start, end, mid = map(int, input().split())
    start, end, mid = start - 1, end - 1, mid - 1
    li = li[:start] + li[mid:end + 1] + li[start:mid] + li[end + 1:]

print(*li)