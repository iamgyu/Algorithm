public class 추억_점수 {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        for (int i = 0; i < photo.length; i++) {
            int total = 0;
            for (String s : photo[i]) {
                for (int j = 0; j < name.length; j++) {
                    if (s.equals(name[j]))
                        total += yearning[j];
                }
                answer[i] = total;
            }
        }

        return answer;
    }
}
