arr = [list(map(int, input().split())) for _ in range(9)]
max_value = -1
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            x, y = i+1, j+1


print(max_value)
print(x, y)