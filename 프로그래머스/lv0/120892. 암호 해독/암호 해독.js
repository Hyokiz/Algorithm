function solution(cipher, code) {
    return cipher.split('').filter((el, i) => {return i % code === code-1}).join('')
}