t = int(input())

for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, max(numbers)))