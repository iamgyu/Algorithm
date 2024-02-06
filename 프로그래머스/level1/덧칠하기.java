public class 덧칠하기 {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int temp = section[0];
        for (int i = 1; i < section.length; i++) {
            if (section[i] > temp + m - 1) {
                answer++;
                temp = section[i];
            }
        }
        answer++;

        return answer;
    }
}
