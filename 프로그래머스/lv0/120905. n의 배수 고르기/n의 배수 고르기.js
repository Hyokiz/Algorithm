function solution(n, numlist) {
    const answer = numlist.filter((i) => {
        return i % n == 0
    })
    return answer;
}