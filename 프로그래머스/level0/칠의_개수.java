package 프로그래머스.level0;

public class 칠의_개수 {
    public int solution(int[] array) {
        int answer = 0;
        for (int i : array) {
            while (i != 0) {
                if(i % 10 == 7)
                    answer++;
                i /= 10;
            }
        }
        return answer;
    }
}
