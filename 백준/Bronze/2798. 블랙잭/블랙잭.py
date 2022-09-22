from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cases = []
for case in combinations(cards, 3):
    if sum(case) <= m:
        cases.append(sum(case))

print(max(cases))