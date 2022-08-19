number = []
for _ in range(10):
    number.append(int(input()))

remain = set()
for i in number:
    remain.add(i % 42)

print(len(remain))