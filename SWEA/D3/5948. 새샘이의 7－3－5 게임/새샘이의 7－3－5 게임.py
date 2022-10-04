from itertools import combinations

for t in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    comb = list(combinations(numbers, 3))
    result = []
    for i in comb:
        if sum(i) not in result:
            result.append(sum(i))

    result.sort(reverse=True)

    print(f'#{t}', result[4])

