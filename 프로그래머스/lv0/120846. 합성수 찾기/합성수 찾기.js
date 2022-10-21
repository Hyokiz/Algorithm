function solution(n) {
    let answer = 0;
    for (i=1; i<=n; i++) {
        let cnt = 0;
        for (j=1; j <= i; j++) {
            if (i % j === 0) {
                cnt += 1
            }
            if (cnt >= 3) {
                answer += 1
                break
            }
        }
    }
    return answer
}