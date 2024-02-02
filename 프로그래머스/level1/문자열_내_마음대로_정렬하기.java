import java.util.Arrays;

public class 문자열_내_마음대로_정렬하기 {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        int cnt = 0;
        Arrays.sort(strings);

        for (int i = 97; i < 123; i++) {
            for (String string : strings) {
                if (string.charAt(n) == (char) i)
                    answer[cnt++] = string;
            }
        }
        return answer;
    }
}
