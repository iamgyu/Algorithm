public class 카드_뭉치 {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int num1 = 0;
        int num2 = 0;
        for (String s : goal) {
            if (num1 < cards1.length) {
                if (s.equals(cards1[num1])) {
                    num1++;
                    continue;
                }
            }

            if (num2 < cards2.length) {
                if (s.equals(cards2[num2])) {
                    num2++;
                    continue;
                }
            }
            return "No";
        }
        return "Yes";
    }
}
