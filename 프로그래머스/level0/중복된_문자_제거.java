package 프로그래머스.level0;

public class 중복된_문자_제거 {
    public String solution(String my_string) {
        String answer = "";
        char[] arr = my_string.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if (!answer.contains(Character.toString(arr[i]))) {
                answer += Character.toString(arr[i]);
            }
        }
        return answer;
    }
}