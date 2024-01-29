import java.util.Arrays;

public class 정수_내림차순으로_배치하기 {
    public long solution(long n) {
        long answer = 0;
        String s = "";
        while (n != 0) {
            s += n % 10;
            n /= 10;
        }

        char[] arr = s.toCharArray();
        Arrays.sort(arr);

        return Long.parseLong(new StringBuilder(new String(arr)).reverse().toString());
    }
}
