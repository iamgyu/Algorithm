import java.util.HashMap;
import java.util.Map;

public class 숫자_문자열과_영단어 {
    public int solution(String s) {
        Map<String, String> map = new HashMap<>(){{
            put("zero", "0");
            put("one", "1");
            put("two", "2");
            put("three", "3");
            put("four", "4");
            put("five", "5");
            put("six", "6");
            put("seven", "7");
            put("eight", "8");
            put("nine", "9");
        }};

        for (String num : map.keySet()) {
            if (s.contains(num)) {
                s = s.replaceAll(num, map.get(num));
            }
        }

        return Integer.parseInt(s);
    }
}
