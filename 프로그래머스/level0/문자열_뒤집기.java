package 프로그래머스.level0;

public class 문자열_뒤집기 {
    public String solution(String my_string) {
        StringBuilder sb = new StringBuilder(my_string);
        sb.reverse();
        return sb.toString();
    }
}
