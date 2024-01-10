package 프로그래머스.level0;

public class 한_번만_등장한_문자 {
    public String solution(String s) {
        String answer = "";
        char[] arr = s.toCharArray();
        int[] numArr = new int[26];
        for (char c : arr) {
            numArr[(int)c - 97]++;
        }

        for (int i = 0; i < numArr.length; i++) {
            if (numArr[i] == 1) {
                answer += Character.toString((char) (i + 97));
            }
        }
        return answer;
    }
}