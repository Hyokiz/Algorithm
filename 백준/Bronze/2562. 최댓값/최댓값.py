number = []
for i in range(9):
    number.append(int(input()))

result = []
for i, num in enumerate(number):
    if num == max(number):
        result.append(num)
        result.append(i)

print(result[0])
print(result[1] + 1)