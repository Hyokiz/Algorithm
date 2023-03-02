n, m = map(int, input().split())
nums = list(range(n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    nums[i:j+1] = nums[i:j+1][::-1]

print(*nums[1:])
