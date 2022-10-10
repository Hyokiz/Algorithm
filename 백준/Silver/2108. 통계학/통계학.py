from collections import Counter

n = int(input())
numbers = list()
result = list()
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
nums = Counter(numbers).most_common()
# 1. 산술평균
print(int(round(sum(numbers)/n, 0)))

# 2. 중앙값
print(numbers[n//2])

# 3. 최빈값
if len(nums) > 1:
    if nums[0][1] == nums[1][1]:
        print(nums[1][0])
    else:
        print(nums[0][0])
else:
    print(nums[0][0])

# 4. 범위
print(abs(max(numbers) - min(numbers)))