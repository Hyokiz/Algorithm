n = int(input())
students = []
for _ in range(n):
    weight, height = map(int, input().split())
    students.append((weight, height))

result = []
for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    result.append(rank)

print(*result)