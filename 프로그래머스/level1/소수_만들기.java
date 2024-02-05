public class 소수_만들기 {
    public int solution(int[] nums) {
        int answer = 0;

        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    int temp = nums[i] + nums[j] + nums[k];
                    if(isPrime(temp))
                        answer++;
                }
            }
        }

        return answer;
    }

    public boolean isPrime(int n) {
        boolean answer = true;

        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                answer = false;
                break;
            }
        }

        return answer;
    }
}
