def calculate(a, b):
    if node[1] == '+':
        return tree[a] + tree[b]
    elif node[1] == '-':
        return tree[a] - tree[b]
    elif node[1] == '*':
        return tree[a] * tree[b]
    else:
        return tree[a] // tree[b]

for t in range(1, 11):
    n = int(input())
    tree = [0] * (n + 1)
    nodes = [list(input().split()) for _ in range(n)]
    for node in nodes[::-1]:
        if len(node) == 2:
            tree[int(node[0])] = int(node[1])
        else:
            tree[int(node[0])] = calculate(int(node[2]), int(node[3]))

    print(f'#{t} {tree[1]}')

