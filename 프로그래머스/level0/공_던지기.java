package 프로그래머스.level0;

public class 공_던지기 {
    public int solution(int[] numbers, int k) {
        return numbers[2 * (k - 1) % numbers.length];
    }
}