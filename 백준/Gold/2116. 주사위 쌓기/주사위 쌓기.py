n = int(input())
dices = []
numbers = list(range(1, 7))
rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

for _ in range(n):
    dices.append(list(map(int, input().split())))

result = []
for i in range(6):
    max_number = []
    temp = list(range(1, 7))
    bottom = dices[0][i]
    top = dices[0][rotate[i]]
    temp.remove(bottom)
    temp.remove(top)
    max_number.append(max(temp))
    for j in range(1, n):
        temp = list(range(1, 7))
        bottom = top
        temp.remove(bottom)
        top = dices[j][rotate[dices[j].index(top)]]
        temp.remove(top)
        max_number.append(max(temp))

    result.append(sum(max_number))

print(max(result))
