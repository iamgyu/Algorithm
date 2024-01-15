package 프로그래머스.level0;

public class 잘라서_배열로_저장하기 {
    public String[] solution(String my_str, int n) {
        int resultCnt = (my_str.length() + n - 1) / n;
        String[] answer = new String[resultCnt];

        for (int i = 0; i < resultCnt; i++) {
            int start = i * n;
            int end;
            if (start + n >= my_str.length()) {
                end = my_str.length();
            } else {
                end = start + n;
            }
            answer[i] = my_str.substring(start, end);
        }
        return answer;
    }
}
