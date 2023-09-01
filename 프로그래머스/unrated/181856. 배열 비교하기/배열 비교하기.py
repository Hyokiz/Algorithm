def solution(arr1, arr2):
    n, m = len(arr1), len(arr2)

    if n > m:
        return 1
    elif n < m:
        return -1
    else:
        i, j = sum(arr1), sum(arr2)
        if i > j:
            return 1
        elif i < j:
            return -1
        else:
            return 0