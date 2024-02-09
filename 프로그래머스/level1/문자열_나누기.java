public class 문자열_나누기 {
    public int solution(String s) {
        int answer = 1;
        int count = 1;
        char c = s.charAt(0);

        for (int i = 1; i < s.length(); i++) {
            if (count == 0) {
                answer++;
                c = s.charAt(i);
            }

            if(c == s.charAt(i))
                count++;
            else
                count--;

        }
        return answer;
    }
}
