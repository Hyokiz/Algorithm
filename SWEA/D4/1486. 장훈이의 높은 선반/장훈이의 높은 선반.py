from itertools import combinations

for t in range(1, int(input()) + 1):
    n, b = map(int, input().split())
    clerk = list(map(int, input().split()))
    combination_list = []
    for i in range(n+1):
        combination_list += combinations(clerk, i)
    result = []
    for i in range(len(combination_list)):
        if sum(combination_list[i]) >= b:
            result.append(sum(combination_list[i]))

    print(f'#{t} {min(result) - b}')