package 프로그래머스.level0;

public class 문자열안에_문자열 {
    public int solution(String str1, String str2) {
        if(str1.contains(str2))
            return 1;
        else
            return 2;
    }
}