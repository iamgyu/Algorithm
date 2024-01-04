package 프로그래머스.level0;

public class 모스부호_1 {
    public String solution(String letter) {
        String[] morse = {
                ".-", "-...", "-.-.", "-..", ".", "..-.",
                "--.", "....", "..", ".---", "-.-", ".-..",
                "--", "-.", "---", ".--.", "--.-", ".-.",
                "...", "-", "..-", "...-", ".--", "-..-",
                "-.--", "--.." };

        String[] letterArr = letter.split(" ");

        StringBuilder sb = new StringBuilder();
        for (String str : letterArr) {
            for (int i = 0; i < morse.length; i++) {
                if (str.equals(morse[i])) {
                    sb.append(Character.toString(i + 'a'));
                }
            }
        }
        return sb.toString();
    }
}