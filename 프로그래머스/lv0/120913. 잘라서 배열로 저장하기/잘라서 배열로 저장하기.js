// function solution(my_str, n) {
//     let res = [];
//     for (let i = 0; i < my_str.length; i+=n) res.push(my_str.slice(i, i+n));
//     return res;
// }

function solution(my_str, n) {
    let answer = [];
    for (i = 0; i < my_str.length; i += n) {
        answer.push(my_str.slice(i, i + n))
    }
    return answer
}