public class 삼진법_뒤집기 {
    public int solution(int n) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            int remainder = n % 3;
            sb.append(remainder);
            n /= 3;
        }

        for (int i = sb.length() - 1; i >= 0; i--)
            answer += (int) ((sb.charAt(i) - '0') * Math.pow(3, sb.length() - i - 1));

        return answer;
    }
}
