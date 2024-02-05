import java.util.Arrays;

public class 과일_장수 {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Arrays.sort(score);
        for (int i = score.length; i >= 0; i -= m) {
            if (i >= m) {
                int[] arr = Arrays.copyOfRange(score, i - m, i);
                answer += Arrays.stream(arr).min().orElse(0) * m;
            }
        }
        return answer;
    }
}
