# 13428. 숫자 조작
from itertools import combinations

for t in range(1, int(input()) + 1):
    n = list(input().strip())
    max_v, min_v = n[:], n[:]

    for i in range(len(n)):
        temp = n[:]
        for j in range(i+1, len(n)):
            temp[i], temp[j] = temp[j], temp[i]

            if max_v < temp:
                max_v = temp[:]

            if min_v > temp and temp[0] != '0':
                min_v = temp[:]

            temp[i], temp[j] = temp[j], temp[i]

    print(f'#{t}', ''.join(min_v), ''.join(max_v))
