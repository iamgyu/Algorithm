public class 옹알이2 {
    public int solution(String[] babbling) {
        int answer = 0;
        for (String s : babbling) {
            s = s.replaceAll("ayaaya|yeye|woowoo|mama", " ");
            s = s.replaceAll("aya|ye|woo|ma", "");
            if(s.isEmpty())
                answer++;
        }
        return answer;
    }
}
