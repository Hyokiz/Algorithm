def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

n = int(input())
m = int(input())
edges = []
for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))

edges.sort()

parent = list(range(n + 1))
counts = 0
costs = 0

for dist, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)

    if x_root != y_root:
        if x_root < y_root:
            parent[y_root] = x_root
            costs += dist
            counts += 1

            if counts >= n - 1:
                break
        
        else:
            parent[x_root] = y_root
            costs += dist
            counts += 1
            
            if counts >= n - 1:
                break

print(costs)