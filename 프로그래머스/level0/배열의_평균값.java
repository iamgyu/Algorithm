package 프로그래머스.level0;

public class 배열의_평균값 {
    public double solution(int[] numbers) {
        double answer = 0;
        for (int n : numbers) {
            answer+= n;
        }

        return (double) Math.round(answer / numbers.length * 10) / 10;
    }
}
