public class 로또의_최고_순위와_최저_순위 {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int[] rank = new int[]{6, 6, 5, 4, 3, 2, 1};

        for (int i = 0; i < lottos.length; i++) {
            if (lottos[i] == 0) {
                answer[0]++;
                continue;
            }
            for (int win : win_nums) {
                if (lottos[i] == win) {
                    answer[0]++;
                    answer[1]++;
                }
            }
        }

        answer[0] = rank[answer[0]];
        answer[1] = rank[answer[1]];

        return answer;
    }
}
