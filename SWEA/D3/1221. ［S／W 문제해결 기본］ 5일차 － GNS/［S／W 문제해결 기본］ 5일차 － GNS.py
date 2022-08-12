t = int(input())

for _ in range(10):
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    x, y = input().split()
    text = list(input().split())
    counter = [0] * 10
    print(x)
    for i in text:
        counter[numbers.index(i)] += 1
    result = ''
    for j in range(10):
        result += (numbers[j] + ' ') * counter[j]

    print(result)