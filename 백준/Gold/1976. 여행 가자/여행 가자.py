# 1976. 여행가자

# 2. find-set
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

# 3. union
def union(x_root, y_root):
    if x_root != y_root:
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root


n = int(input())
m = int(input())
# 1. make-set
parent = list(range(n + 1))

for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == '1':
            i_root, j_root = find_set(i + 1), find_set(j + 1)
            union(i_root, j_root)

plans = list(map(int, input().split()))
# plans 의 루트를 먼저 찾는다.
root = find_set(plans[0])
result = 'YES'

# 첫번째 도시의 대표값과 같으면 같은 집합
for i in range(1, m):
    if root != find_set(plans[i]):
        result = 'NO'
        break

print(result)