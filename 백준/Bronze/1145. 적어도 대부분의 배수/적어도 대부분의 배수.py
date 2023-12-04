# 1145. 적어도 대부분의 배수
from itertools import combinations
from math import lcm
import sys

nums = list(map(int, input().split()))
answer = sys.maxsize

for combs in combinations(nums, 3):
    answer = min(answer, lcm(*combs))

print(answer)