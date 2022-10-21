function solution(box, n) {
    return box.map((el) => { return Math.floor(el / n) }).reduce((sum, i) => { return sum * i}, 1)
}