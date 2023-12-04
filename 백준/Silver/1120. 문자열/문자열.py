# 1120. 문자열

a, b = input().split()
answer = 50
if len(a) < len(b):
    for i in range(len(b) - len(a) + 1):
        tmp = 0
        for j in range(len(a)):
            if b[i + j] != a[j]:
                tmp += 1

        answer = min(answer, tmp)

elif len(a) > len(b):
    for i in range(len(a) - len(b) + 1):
        tmp = 0
        for j in range(len(b)):
            if a[i + j] != b[j]:
                tmp += 1

        answer = min(answer, tmp)

else:
    tmp = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            tmp += 1

    answer = min(answer, tmp)

print(answer)