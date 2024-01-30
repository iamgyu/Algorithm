public class 최대공약수와_최소공배수 {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        answer[0] = gcd(n, m);
        answer[1] = n * m / gcd(n, m);
        return answer;
    }

    public int gcd(int n, int m) {
        int temp = 0;
        int max = Math.max(n, m);
        int min = Math.min(n, m);
        while (min != 0) {
            temp = max % min;
            max = min;
            min = temp;
        }
        return max;
    }
}
