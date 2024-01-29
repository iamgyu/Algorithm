public class 없는_숫자_더하기 {
    public int solution(int[] numbers) {
        int answer = 0;
        for (int n : numbers) {
            answer += n;
        }
        return 45 - answer;
    }
}
