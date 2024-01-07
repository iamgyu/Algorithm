package 프로그래머스.level0;

    import java.util.Arrays;

public class 문자열_정렬하기_1 {
    public int[] solution(String my_string) {
        char[] c = my_string.replaceAll("[^0-9]", "").toCharArray();
        int[] answer = new int[c.length];
        for (int i = 0; i < c.length; i++) {
            answer[i] = Character.digit(c[i], 10);
        }
        Arrays.sort(answer);
        return answer;
    }
}
