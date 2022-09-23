import sys

n = int(input())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

cards_dict = {}
for i in range(len(cards)):
    cards_dict[cards[i]] = 0

for j in range(m):
    if check[j] in cards_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')