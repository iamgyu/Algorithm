public class 부족한_금액_계산하기 {
    public long solution(int price, int money, int count) {
        long total = 0;
        for (int i = 1; i <= count; i++) {
            total += (long)price * i;
        }
        if(money > total)
            return 0;
        return Math.abs(money - total);
    }
}
