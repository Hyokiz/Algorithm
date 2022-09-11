n = int(input())

numbers = []
for _ in range(n):

    numbers.append(int(input()))

numbers = sorted(numbers)

for i in numbers:
    print(i)