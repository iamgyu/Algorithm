package 프로그래머스.level0;

public class 치킨_쿠폰 {
    public int solution(int chicken) {
        int answer = 0;
        while (chicken >= 10) {
            int coupon_chicken = chicken / 10;
            int remain_coupon = chicken % 10;
            answer += coupon_chicken;
            chicken = coupon_chicken + remain_coupon;
        }
        return answer;
    }
}
