# 18870. 좌표 압축

n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(list(set(numbers)))
dic = {sorted_numbers[i] : i for i in range(len(sorted_numbers))}

for i in numbers:
    print(dic[i], end=' ')