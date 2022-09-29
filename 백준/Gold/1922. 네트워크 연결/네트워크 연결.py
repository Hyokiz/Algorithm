import sys

def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])   # 경로 압축
    return parent[node]


n = int(sys.stdin.readline())    # 컴퓨터 수
m = int(sys.stdin.readline())    # 연결의 수
network = []

for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split()) # 시작, 도착 ,비용
    network.append((w, s, e))

network.sort()  # 비용 기준 정렬(오름차순)
parent = list(range(n + 1))
counts = 0  # 더 이상 간선을 선택하지 않아도 되는 때 판별
cost = 0    # 총 비용(최소가 되는 값 찾기)

for w, x, y in network:
    x_root, y_root = find_set(x), find_set(y)

    # Union
    if x_root != y_root:
        parent[min(x_root, y_root)] = max(x_root, y_root)
        counts += 1
        cost += w

        if counts >= n - 1:
            break

print(cost)
