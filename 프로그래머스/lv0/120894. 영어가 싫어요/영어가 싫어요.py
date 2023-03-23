def solution(numbers):
    english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, s in enumerate(english):
        numbers = numbers.replace(s, str(i))
    return int(numbers)