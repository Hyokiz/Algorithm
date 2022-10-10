# 1427. 소트인사이드

n = list(map(int, input()))
n.sort(reverse=True)
print(''.join(map(str, n)))
