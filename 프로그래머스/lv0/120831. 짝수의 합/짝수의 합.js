function solution(n) {
    let sumValue = 0;
    for (let i=1; i <= n; i++) {
        if (i % 2 == 0) {
            sumValue += i
        }
    }
    return sumValue
}