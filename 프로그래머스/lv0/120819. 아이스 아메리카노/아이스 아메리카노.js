function solution(money) {
    var answer = [];
    const canBuy = Math.floor(money / 5500)
    answer.push(canBuy)
    answer.push(money - (5500 * canBuy))
    return answer;
}