from itertools import combinations
from math import sqrt

def solution(nums):
    answer = 0

    
    for combs in combinations(nums, 3):
        s = sum(combs)

        for i in range(2, int(sqrt(s)) + 2):
            if s % i == 0:
                break
        else:
            answer += 1

    return answer