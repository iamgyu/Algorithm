package 프로그래머스.level0;

public class 옹알이_1 {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] word = new String[]{"aya", "ye", "woo", "ma"};
        for (int i = 0; i < babbling.length; i++) {
            for (String string : word) {
                if (babbling[i].contains(string)) {
                    babbling[i] = babbling[i].replace(string, " ");
                }
            }
        }

        for (String s : babbling) {
            s = s.replace(" ", "");
            if(s.isEmpty())
                answer++;
        }
        return answer;
    }
}
