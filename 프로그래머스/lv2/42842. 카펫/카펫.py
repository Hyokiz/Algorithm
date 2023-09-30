def solution(brown, yellow):
    li = []
    for i in range(1, int(yellow ** (1/2)) + 1):
        if yellow % i == 0:
            x, y = 0, 0
            if (i ** 2) != yellow:
                x, y = (yellow // i) + 2, i + 2
            else:
                x, y = i + 2, i + 2
            
            if (x * y) - yellow == brown:
                return [x, y]
