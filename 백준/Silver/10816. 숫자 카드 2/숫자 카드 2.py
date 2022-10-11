# 10816. 숫자 카드 2
from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find_card = list(map(int, input().split()))

counter = Counter(cards)

for i in find_card:
    if i in counter:
        print(counter[i], end=' ')
    else:
        print(0, end=' ')