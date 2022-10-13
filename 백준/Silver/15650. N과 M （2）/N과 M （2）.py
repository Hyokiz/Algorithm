# 15650. n과 m
from itertools import combinations

n, m = map(int, input().split())
comb = list(range(1, n + 1))
for case in combinations(comb, m):
    print(*case)