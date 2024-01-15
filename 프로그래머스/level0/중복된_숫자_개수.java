package 프로그래머스.level0;

public class 중복된_숫자_개수 {
    public int solution(int[] array, int n) {
        int answer = 0;
        for (int i : array) {
            if(i == n)
                answer++;
        }
        return answer;
    }
}
