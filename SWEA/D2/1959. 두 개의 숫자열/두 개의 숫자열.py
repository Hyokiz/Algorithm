# 1959. 두 개의 숫자열

def sol(x, y, arr_x, arr_y):
    result = 0
    for i in range(y - x + 1):
        max_value = 0
        for j in range(x):
            temp = arr_x[j] * arr_y[i+j]
            max_value += temp

        if result < max_value:
            result = max_value

    return result


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))

    if n < m:
        print(f'#{t}', sol(n, m, num1, num2))
    else:
        print(f'#{t}', sol(m, n, num2, num1))