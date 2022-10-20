function solution(n) {
    let answer = 0
    if (n > 0) {
        const arr = Array.from({length : n + 1}, (_, i) => i + 1)
        const divisor = arr.filter((el) => {
            return n % el === 0
        })
        let answer = divisor.reduce((sum, x) => {
            return sum + x
        }, 0)
        return answer
    } 
    return answer
}