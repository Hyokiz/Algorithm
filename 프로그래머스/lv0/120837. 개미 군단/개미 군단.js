function solution(hp) {
    let answer = 0
    while (hp > 0) {
        if (hp >= 5) {
            const captain = Math.floor(hp / 5)
            answer += captain
            hp -= 5 * captain
            continue
        } else if (hp >= 3) {
            const soldier = Math.floor(hp / 3)
            answer += soldier
            hp -= 3 * soldier
            continue
        } else {
            const worker = hp
            answer += worker
            hp -= worker
        }
    }
    return answer;
}