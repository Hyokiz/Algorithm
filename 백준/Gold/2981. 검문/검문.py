import sys
import math

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))

M = []
for i in range(len(nums)-1):
    M.append(abs(nums[i] - nums[i+1]))
M.sort()

gcd = M[0]
for i in range(1, len(M)-1):
    gcd = math.gcd(gcd, M[i])

result = []

for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)
result.append(gcd)

for i in sorted(set(result)):
    print(i, end = " ")