public class 다트게임 {
    public int solution(String dartResult) {
        int answer = 0;

        String[] arr = dartResult.split("");
        int[] score = new int[3];

        int idx = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].matches("[0-9]")) {
                idx++;
                score[idx] = Integer.parseInt(arr[i]);
                if (arr[i + 1].matches("[0-9]")) {
                    score[idx] *= 10;
                    i++;
                }
            }

            switch (arr[i]) {
                case "D":
                    score[idx] = (int) Math.pow(score[idx], 2);
                    break;
                case "T":
                    score[idx] = (int) Math.pow(score[idx], 3);
                    break;
                case "*":
                    score[idx] *= 2;
                    if(idx - 1 >= 0) score[idx - 1] *= 2;
                    break;
                case "#":
                    score[idx] *= -1;
            }
        }
        for(int s : score)
            answer += s;

        return answer;
    }
}
