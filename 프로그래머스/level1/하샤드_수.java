public class 하샤드_수 {
    public boolean solution(int x) {
        int temp = 0;
        int n = x;
        while (n != 0) {
            temp += n % 10;
            n /= 10;
        }

        if(x % temp == 0)
            return true;
        else
            return false;
    }
}
