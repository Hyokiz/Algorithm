def solution(price, money, count):
    answer = money - (sum(list(range(1, count + 1))) * price)
    return -answer if answer < 0 else 0
