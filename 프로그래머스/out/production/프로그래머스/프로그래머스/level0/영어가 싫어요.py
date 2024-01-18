def solution(numbers):
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, num in enumerate(arr):
        numbers = numbers.replace(num, str(i))
    return int(numbers)