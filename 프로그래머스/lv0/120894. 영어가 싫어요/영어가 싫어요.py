def solution(numbers):
    s = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        numbers = numbers.replace(s[i], str(i))
    return int(numbers)