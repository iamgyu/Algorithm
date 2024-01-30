import java.util.Arrays;

public class 문자열_내림차순으로_배치하기 {
    public String solution(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder(new String(arr));

        return sb.reverse().toString();
    }
}
