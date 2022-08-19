number = set(range(1, 10001))
generated_number = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_number.add(i)

result = sorted(number - generated_number)
for i in result:
    print(i)