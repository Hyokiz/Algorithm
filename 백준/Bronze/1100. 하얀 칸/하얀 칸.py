# 1100. 하얀 칸

chess = [list(input()) for _ in range(8)]
answer = 0
for i in range(8):
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if chess[i][j] == "F":
                answer += 1
    else:
        for j in range(1, 8, 2):
            if chess[i][j] == "F":
                answer += 1

print(answer)