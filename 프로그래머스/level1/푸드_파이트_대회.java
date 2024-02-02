public class 푸드_파이트_대회 {
    public String solution(int[] food) {
        StringBuilder sb = new StringBuilder();
        StringBuilder temp = new StringBuilder();
        for (int i = 1; i < food.length; i++) {
            for (int j = 0; j < food[i] / 2; j++) {
                temp.append(i);
            }
        }
        sb.append(temp);
        sb.append(0);
        sb.append(temp.reverse());
        return sb.toString();
    }
}
