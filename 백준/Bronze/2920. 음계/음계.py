ascending = list(range(1, 9))
descending = list(range(8, 0, -1))

nums = list(map(int, input().split()))
if nums == ascending:
    print('ascending')
elif nums == descending:
    print('descending')
else:
    print('mixed')