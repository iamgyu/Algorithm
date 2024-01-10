package 프로그래머스.level0;

public class 영어가_싫어요 {
    public long solution(String numbers) {
        String[] arr = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (int i = 0; i < arr.length; i++) {
            if (numbers.contains(arr[i])) {
                numbers = numbers.replace(arr[i], Integer.toString(i));
            }
        }
        return Long.parseLong(numbers);
    }
}