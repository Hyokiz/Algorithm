def solution(a, d, included):
    li = list(range(a, a + d * len(included), d))
    return sum(li[i] for i in range(len(li)) if included[i])