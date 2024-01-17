package 프로그래머스.level0;

public class 숨어있는_숫자의_덧셈_2 {
    public int solution(String my_string) {
        int answer = 0;
        String[] arr = my_string.split("[a-zA-Z]+");
        for (String s : arr) {
            if(!s.isEmpty())
                answer += Integer.parseInt(s);
        }
        return answer;
    }
}
