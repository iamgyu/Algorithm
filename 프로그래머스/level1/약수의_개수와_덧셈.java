public class 약수의_개수와_덧셈 {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i <= right; i++) {
            if(divisor(i) % 2 == 0)
                answer += i;
            else
                answer -= i;
        }
        return answer;
    }

    public int divisor(int n) {
        int result = 0;
        for (int i = 1; i <= n; i++) {
            if(n % i == 0)
                result++;
        }
        return result;
    }
}
