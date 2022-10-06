# 14361. 숫자가 같은 배수
from itertools import permutations

for t in range(1, int(input()) + 1):
    n = list(input())
    m = int(''.join(n))
    perm = list(permutations(n))
    nums = []
    for i in perm:
        temp = ''.join(i)
        if int(temp) % m == 0 and int(temp) != m:
            nums.append(temp)

    if nums:
        print(f'#{t} possible')
    else:
        print(f'#{t} impossible')