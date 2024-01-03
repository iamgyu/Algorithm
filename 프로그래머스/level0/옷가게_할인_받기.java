package 프로그래머스.level0;

public class 옷가게_할인_받기 {
    public int solution(int price) {
        if(price >= 100000 && price < 300000)
            return price * 95 / 100;
        else if(price >= 300000 && price < 500000)
            return price * 90 / 100;
        else if(price >= 500000)
            return price * 80 / 100;
        else
            return price;
    }
}
