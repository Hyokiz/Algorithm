# 1961. 숫자 배열 회전
def rotate(arr, n):
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[n-1-j][i]

    return new_arr

for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr_a = rotate(arr, n)
    arr_b = rotate(arr_a, n)
    arr_c = rotate(arr_b, n)

    print(f'#{t}')
    for r in range(n):
        print(''.join(map(str, arr_a[r])), end=' ')
        print(''.join(map(str, arr_b[r])), end=' ')
        print(''.join(map(str, arr_c[r])), end=' ')
        print()