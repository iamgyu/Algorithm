package 프로그래머스.level0;

public class 문자열_정렬하기_2 {
    public String solution(String my_string) {
        return my_string.toLowerCase()
                .chars()
                .sorted()
                .collect(StringBuilder::new,
                        StringBuilder::appendCodePoint,
                        StringBuilder::append)
                .toString();
    }
}
