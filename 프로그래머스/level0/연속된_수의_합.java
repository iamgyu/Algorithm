package 프로그래머스.level0;

public class 연속된_수의_합 {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        if (num % 2 != 0) {
            for (int i = 0; i < num; i++) {
                answer[i] = total / num + (i - num / 2);
            }
        } else {
            for (int i = 0; i < num; i++) {
                answer[i] = total / num + (i - num / 2) + 1;
            }
        }
        return answer;
    }
}
