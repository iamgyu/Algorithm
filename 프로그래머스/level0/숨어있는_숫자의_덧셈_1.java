package 프로그래머스.level0;

public class 숨어있는_숫자의_덧셈_1 {
    public int solution(String my_string) {
        int answer = 0;
        String s = my_string.replaceAll("[^0-9]", "");
        for (char c : s.toCharArray()) {
            answer += Character.digit(c, 10);
        }
        return answer;
    }
}
