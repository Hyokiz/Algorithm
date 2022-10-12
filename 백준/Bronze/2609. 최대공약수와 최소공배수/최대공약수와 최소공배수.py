# 2609. 최대공약수와 최소공배수

n, m = map(int, input().split())

temp1, temp2 = 0, 0
for i in range(10000, 0, -1):
    if n % i == 0 and m % i == 0:
        temp1 = i
        temp2 = (n // i) * (m // i) * i
        break

print(temp1)
print(temp2)
