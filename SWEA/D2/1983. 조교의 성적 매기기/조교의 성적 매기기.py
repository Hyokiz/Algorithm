# 1983. 조교의 성적 매기기
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    scores = []
    for _ in range(n):
        mid, final, report = map(int, input().split())
        total = (mid * 0.35) + (final * 0.45) + (report * 0.2)
        scores.append(total)

    k_score = scores[k-1]
    scores.sort(reverse=True)

    cnt = n//10
    k_grade = scores.index(k_score) // cnt

    print(f'#{t}', grades[k_grade])