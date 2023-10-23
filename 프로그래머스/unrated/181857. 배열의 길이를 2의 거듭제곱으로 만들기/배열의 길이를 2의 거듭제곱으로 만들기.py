import math

def solution(arr):
    for i in range(11):
        if len(arr) <= int(math.pow(2, i)):
            return arr + [0] * (int(math.pow(2, i)) - len(arr))