function solution(age) {
  return age.toString().split('').map((el) => 'abcdefghij'[el]).join('')
}