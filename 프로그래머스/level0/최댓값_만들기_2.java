package 프로그래머스.level0;

public class 최댓값_만들기_2 {
    public int solution(int[] numbers) {
        int max = -100000000;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if(numbers[i] * numbers[j] > max)
                    max = numbers[i] * numbers[j];
            }
        }
        return max;
    }
}
