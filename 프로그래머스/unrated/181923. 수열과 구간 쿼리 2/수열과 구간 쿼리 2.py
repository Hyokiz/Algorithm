def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        values = set()
        for i in range(s, e + 1):
            if arr[i] > k:
                values.add(arr[i])
        if values:
            answer.append(min(values))
        else:
            answer.append(-1)
    return answer