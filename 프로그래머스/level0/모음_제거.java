package 프로그래머스.level0;

public class 모음_제거 {
    public String solution(String my_string) {
        return my_string.replaceAll("[aeiou]", "");
    }
}