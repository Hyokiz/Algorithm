from itertools import combinations

def solution(balls, share):
    result = 1
    for i in range(share):
        result *= (balls - i)
        result /= 1 + i
        
    return int(result)