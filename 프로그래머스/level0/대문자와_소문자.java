package 프로그래머스.level0;

public class 대문자와_소문자 {
    public String solution(String my_string) {
        String answer = "";
        char[] arr = my_string.toCharArray();
        for (char c : arr) {
            if ((int) c > 64 && (int) c < 91) {
                answer += Character.toString(c + 32);
            } else {
                answer += Character.toString(c - 32);
            }
        }
        return answer;
    }
}