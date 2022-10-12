from itertools import permutations

n, m = map(int, input().split())
nums = list(range(1, n + 1))

for case in permutations(nums, m):
    print(*case)