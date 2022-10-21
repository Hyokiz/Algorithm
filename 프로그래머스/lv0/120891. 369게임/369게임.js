function solution(order) {
    order = (order+'').split('').filter((x) => {return x === '3' || x === '6' || x === '9' })
    return order.length
}