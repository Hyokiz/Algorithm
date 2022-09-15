def inorder(node):
    global result
    if node != 0:
        inorder(tree[node][0])
        result += words[node]
        inorder(tree[node][1])


for t in range(1, 11):
    n = int(input())
    tree = [[0] * 3 for _ in range(n + 1)]
    words = [''] * (n + 1)

    for _ in range(n):
        info = list(input().split())
        words[int(info[0])] = info[1]

        if len(info) > 2:
            tree[int(info[0])][0] = int(info[2])
            if len(info) > 3:
                tree[int(info[0])][1] = int(info[3])

    result = ''
    inorder(1)
    print(f'#{t} {result}')

