package 프로그래머스.level0;

public class 암호해독 {
    public String solution(String cipher, int code) {
        String answer = "";
        char[] arr = cipher.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if ((i + 1) % code == 0) {
                answer += Character.toString(arr[i]);
            }
        }
        return answer;
    }
}