def solution(sizes):
    xs, ys = [], []
    for i, j in sizes:
        xs.append(max(i, j))
        ys.append(min(i, j))
    print(xs, ys)
    return max(xs) * max(ys)