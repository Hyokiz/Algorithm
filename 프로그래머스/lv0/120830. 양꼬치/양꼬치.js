function solution(n, k) {
    const drink = k - parseInt(n / 10)
    return (12000 * n + 2000 * drink)
}