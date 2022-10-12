# 2477. 참외밭

n = int(input())

max_w, max_h = 0, 0
max_w_idx, max_h_idx = 0, 0
li = list()
for i in range(6):
    temp = list(map(int, input().split()))
    li.append(temp)
    if temp[0] == 1 or temp[0] == 2:
        if max_w < temp[1]:
            max_w = temp[1]
            max_w_idx = i

    elif temp[0] == 3 or temp[0] == 4:
        if max_h < temp[1]:
            max_h = temp[1]
            max_h_idx = i

adj = [li[(max_w_idx-1) % 6], li[(max_w_idx + 1) % 6], li[(max_h_idx - 1) % 6], li[(max_h_idx + 1) % 6]]
ans = 1
for i in li:
    if i not in adj:
        ans *= i[1]

result = (max_w * max_h - ans) * n
print(result)