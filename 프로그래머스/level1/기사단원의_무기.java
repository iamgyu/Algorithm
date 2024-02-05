public class 기사단원의_무기 {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            if(measure(i) > limit)
                answer += power;
            else
                answer += measure(i);
        }
        return answer;
    }

    public int measure(int n){
        int count = 0;

        for (int i = 1; i * i <= n; i++) {
            if(i * i == n) count++;
            else if(n % i == 0) count += 2;
        }
        return count;
    }
}
