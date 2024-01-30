public class 가운데_글자_가져오기 {
    public String solution(String s) {
        String answer = "";
        char[] arr = s.toCharArray();
        if (s.length() % 2 == 0)
            answer += Character.toString(arr[s.length() / 2 - 1]) +
                    arr[s.length() / 2];
        else
            answer += arr[s.length() / 2];

        return answer;
    }
}
